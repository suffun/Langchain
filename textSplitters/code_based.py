from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code = """
def hello():
    print("Hello, World!")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""

splitter = RecursiveCharacterTextSplitter.from_language(
     language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=20
)
result = splitter.split_text(code)
print(result[0])

# python code_based.py