import json
from pathlib import Path

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import (
    LoraConfig,
    get_peft_model
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_FILE = (
    PROJECT_ROOT
    / "configs"
    / "lora_config.json"
)

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "lora_training.jsonl"
)


def load_config():

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def build_text(example):

    instruction = example["instruction"]
    input_text = example["input"]
    output = example["output"]

    if input_text:

        text = (
            f"Instruction: {instruction}\n"
            f"Input: {input_text}\n"
            f"Response: {output}"
        )

    else:

        text = (
            f"Instruction: {instruction}\n"
            f"Response: {output}"
        )

    return {
        "text": text
    }


def main():

    config = load_config()

    base_model = config["base_model"]

    output_dir = (
        PROJECT_ROOT
        / config["output_dir"]
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"Loading base model: {base_model}"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        base_model
    )

    model = AutoModelForCausalLM.from_pretrained(
    base_model,
    low_cpu_mem_usage=True
    )

    if tokenizer.pad_token is None:

        tokenizer.pad_token = (
            tokenizer.eos_token
        )

    dataset = load_dataset(
        "json",
        data_files=str(DATA_FILE)
    )

    dataset = dataset.map(
        build_text
    )

    def tokenize(example):

        return tokenizer(
            example["text"],
            truncation=True,
            max_length=512
        )

    tokenized = dataset.map(
        tokenize,
        batched=True
    )

    lora_config = LoraConfig(
        r=config["lora_r"],
        lora_alpha=config["lora_alpha"],
        lora_dropout=config["lora_dropout"],
        target_modules=config["target_modules"],
        bias="none",
        task_type="CAUSAL_LM"
    )

    model = get_peft_model(
        model,
        lora_config
    )

    model.print_trainable_parameters()

    training_args = TrainingArguments(
    output_dir=str(output_dir),
    num_train_epochs=config["epochs"],
    learning_rate=config["learning_rate"],
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    logging_steps=1,
    save_strategy="epoch",
    report_to="none",
    fp16=False
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        data_collator=DataCollatorForLanguageModeling(
            tokenizer=tokenizer,
            mlm=False
        )
    )

    trainer.train()

    model.save_pretrained(
        output_dir
    )

    tokenizer.save_pretrained(
        output_dir
    )

    print(
        f"\nLoRA adapter saved to:\n{output_dir}"
    )


if __name__ == "__main__":
    main()