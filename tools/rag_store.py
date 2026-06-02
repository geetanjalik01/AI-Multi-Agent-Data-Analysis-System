import chromadb

from sentence_transformers import SentenceTransformer


client = chromadb.Client()

collection = client.create_collection(
    name="reports"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def store_report(report_text, report_id):

    embedding = model.encode(report_text).tolist()

    collection.add(
        documents=[report_text],
        embeddings=[embedding],
        ids=[report_id]
    )


def search_reports(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results