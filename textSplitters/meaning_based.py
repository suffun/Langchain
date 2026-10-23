from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text = """
Python is a high-level programming language.
Python has a simple and readable syntax.
It is widely used for web development and automation.

Machine learning is a branch of artificial intelligence.
It allows computers to learn patterns from data.
Neural networks are commonly used in machine learning.

React is a JavaScript library for building user interfaces.
It is commonly used to create frontend web applications.
"""

docs = splitter.create_documents([text])

print(len(docs))
print(docs)