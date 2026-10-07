from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="Qwen/Qwen3-Embedding-0.6B",
    task="feature-extraction",
)
documents = [
    "delhi is the capital of india",
    "prime minsiter of india",
    "mango is eaten in summer",
    "sweets is eaten in fesitivals"
    ]
query = "which fruit is eaten in summer"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings) [0]

index,score =sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]
print(query)
print(documents[index])
print("Similarity Score is :",score)


# Qwen/Qwen3-Embedding-0.6B