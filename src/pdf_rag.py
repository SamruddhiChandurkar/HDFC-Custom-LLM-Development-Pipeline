import json
import re
from pathlib import Path

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


PROJECT_ROOT = Path(__file__).resolve().parent.parent

PDF_STORAGE = PROJECT_ROOT / "data" / "uploaded_policies"
PDF_INDEX_FILE = PROJECT_ROOT / "data" / "pdf_rag_index.json"


class PDFPolicyRAG:

    def __init__(self):

        PDF_STORAGE.mkdir(
            parents=True,
            exist_ok=True
        )

        self.documents = self.load_index()

        self.vectorizer = None
        self.matrix = None

        self.rebuild_index()

    # -----------------------------------------
    # Index storage
    # -----------------------------------------

    def load_index(self):

        if not PDF_INDEX_FILE.exists():
            return []

        try:

            with open(
                PDF_INDEX_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except Exception:

            return []

    def save_index(self):

        PDF_INDEX_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            PDF_INDEX_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.documents,
                file,
                indent=4,
                ensure_ascii=False
            )

    # -----------------------------------------
    # Text cleaning
    # -----------------------------------------

    def clean_text(self, text):

        text = text.replace(
            "\x00",
            " "
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    # -----------------------------------------
    # PDF extraction
    # -----------------------------------------

    def extract_pdf_text(
        self,
        pdf_path
    ):

        reader = PdfReader(
            str(pdf_path)
        )

        pages = []

        for page_number, page in enumerate(
            reader.pages,
            start=1
        ):

            text = page.extract_text() or ""

            text = self.clean_text(
                text
            )

            if text:

                pages.append({
                    "page": page_number,
                    "text": text
                })

        return pages

    # -----------------------------------------
    # Chunking
    # -----------------------------------------

    def create_chunks(
        self,
        pages,
        chunk_size=1200,
        overlap=200
    ):

        chunks = []

        for page in pages:

            text = page["text"]

            start = 0

            while start < len(text):

                end = start + chunk_size

                chunk = text[start:end]

                if chunk.strip():

                    chunks.append({
                        "page": page["page"],
                        "text": chunk
                    })

                start += (
                    chunk_size - overlap
                )

        return chunks

    # -----------------------------------------
    # Add PDF
    # -----------------------------------------

    def add_pdf(
        self,
        uploaded_file
    ):

        filename = uploaded_file.name

        safe_name = re.sub(
            r"[^a-zA-Z0-9._-]",
            "_",
            filename
        )

        pdf_path = (
            PDF_STORAGE / safe_name
        )

        with open(
            pdf_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )

        pages = self.extract_pdf_text(
            pdf_path
        )

        if not pages:

            raise ValueError(
                "No readable text was found in the PDF."
            )

        chunks = self.create_chunks(
            pages
        )

        document_id = (
            f"PDF-{len(self.documents) + 1:04d}"
        )

        for index, chunk in enumerate(
            chunks
        ):

            self.documents.append({

                "document_id": document_id,

                "filename": safe_name,

                "chunk_id": index + 1,

                "page": chunk["page"],

                "text": chunk["text"]

            })

        self.save_index()

        self.rebuild_index()

        return {
            "document_id": document_id,
            "filename": safe_name,
            "pages": len(pages),
            "chunks": len(chunks)
        }

    # -----------------------------------------
    # Rebuild retrieval index
    # -----------------------------------------

    def rebuild_index(self):

        if not self.documents:

            self.vectorizer = None
            self.matrix = None

            return

        texts = [
            item["text"]
            for item in self.documents
        ]

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            max_features=10000
        )

        self.matrix = (
            self.vectorizer.fit_transform(
                texts
            )
        )

    # -----------------------------------------
    # Search
    # -----------------------------------------

    def search(
        self,
        query,
        top_k=5
    ):

        if (
            not self.documents
            or self.vectorizer is None
        ):

            return []

        query_vector = (
            self.vectorizer.transform(
                [query]
            )
        )

        similarities = cosine_similarity(
            query_vector,
            self.matrix
        )[0]

        ranked_indexes = similarities.argsort()[
            ::-1
        ]

        results = []

        for index in ranked_indexes[:top_k]:

            score = float(
                similarities[index]
            )

            if score <= 0:
                continue

            document = self.documents[
                index
            ]

            results.append({

                "document_id":
                    document["document_id"],

                "filename":
                    document["filename"],

                "page":
                    document["page"],

                "chunk_id":
                    document["chunk_id"],

                "text":
                    document["text"],

                "score":
                    round(score, 4)

            })

        return results

    # -----------------------------------------
    # Stats
    # -----------------------------------------

    def get_documents(self):

        documents = {}

        for item in self.documents:

            document_id = item[
                "document_id"
            ]

            if document_id not in documents:

                documents[document_id] = {
                    "document_id": document_id,
                    "filename": item["filename"],
                    "chunks": 0
                }

            documents[
                document_id
            ]["chunks"] += 1

        return list(
            documents.values()
        )