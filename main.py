
# HDFC Custom LLM Development Pipeline
# Project ka first Python program

project_name = "HDFC Custom LLM Pipeline"

bank_name = "HDFC Bank"

project_status = "Setup Started"

print("=" * 50)

print("WELCOME TO", project_name)

print("=" * 50)

print("Bank:", bank_name)

print("Project Status:", project_status)

print("Purpose: Governed Banking LLM Development")

print("Environment: Local Development")

print("Data Type: Synthetic Demo Data Only")

print("=" * 50)

print("First Python Program Successfully Executed!")

from src.data_validator import validate_dataset


print("=" * 55)
print("HDFC CUSTOM LLM - DATA GOVERNANCE MODULE")
print("=" * 55)

dataset_path = "data/banking_records.json"

print("\nChecking dataset...")
print("File:", dataset_path)

result = validate_dataset(dataset_path)

print("\nVALIDATION RESULT")
print("-" * 55)

if result["valid"]:

    print("Status: PASSED")
    print("Dataset ID:", result["dataset_id"])
    print("Total Records:", result["record_count"])

    print("\nDataset passed the demo validation checks.")

else:

    print("Status: FAILED")

    print("\nErrors found:")

    for error in result["errors"]:
        print("-", error)

print("\n" + "=" * 55)
print("END OF DATA VALIDATION")
print("=" * 55)
