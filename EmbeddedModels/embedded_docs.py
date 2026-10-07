from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "delhi is the capital of india",
    "prime minsiter of india",
    "mango",
    "sweets"
    ]
vector = embedding.embed_documents(documents)
print(str(vector))

# python EmbeddedModels/embedded_docs.py