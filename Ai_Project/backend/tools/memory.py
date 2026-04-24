from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from backend.config import COHERE_API_KEY

# ✅ Correct API key usage
embeddings = CohereEmbeddings(
    cohere_api_key=COHERE_API_KEY,
    model="embed-english-v3.0"
)

# ✅ FAISS must NOT be empty
db = FAISS.from_texts(["initial memory"], embeddings)


def save_memory(text):
    if text and text.strip():
        try:
            print("Saving text:", text)
            db.add_texts([text])
        except Exception as e:
            print("Error saving memory:", e)


def search_memory(query):
    try:
        docs = db.similarity_search(query, k=3)
        return [d.page_content for d in docs]
    except Exception as e:
        print("Error searching memory:", e)
        return []