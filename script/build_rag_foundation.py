from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import os
import tiktoken
import chromadb

# ================================
# 1) Load Markdown Corpus
# ================================
corpus_dir = "data/corpus"
documents = []

for filename in os.listdir(corpus_dir):
    if filename.endswith(".md"):
        with open(os.path.join(corpus_dir, filename), "r", encoding="utf-8") as f:
            documents.append({
                "filename": filename,
                "text": f.read()
            })

print(f"[OK] Loaded documents: {len(documents)}")

# ================================
# 2) Chunking
# ================================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

chunks = []
for doc in documents:
    cks = splitter.split_text(doc["text"])
    for i, ck in enumerate(cks):
        chunks.append({
            "id": f"{doc['filename']}_chunk_{i}",
            "text": ck,
            "filename": doc["filename"]
        })

print(f"[OK] Total chunks created: {len(chunks)}")


# ================================
# 3) Embeddings
# ================================
model = SentenceTransformer("all-MiniLM-L6-v2")
print("[OK] Embedding model loaded")

for ch in chunks:
    ch["embedding"] = model.encode(ch["text"]).tolist()

print("[OK] Embeddings created successfully")

# ================================
# 4) Create VectorDB (Chroma)
# ================================
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_or_create_collection(name="policies")

for ch in chunks:
    collection.add(
        ids=[ch["id"]],
        embeddings=[ch["embedding"]],
        documents=[ch["text"]],
        metadatas=[{"filename": ch["filename"]}]
    )

print("[OK] Vector DB created and populated!")



# جلب كل الـ documents
results = collection.get(include=["documents"])

enc = tiktoken.get_encoding("cl100k_base")

for doc, id in zip(results["documents"], results["ids"]):
    tokens = len(enc.encode(doc))
    print(f"{id} -> {tokens} tokens")