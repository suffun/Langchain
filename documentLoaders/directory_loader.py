from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


loader = DirectoryLoader(
    path='cricket_data',
    glob = '*.txt',
    loader_cls = TextLoader
)

docs = loader.load()


print((docs[0]))

# print((docs[0].metadata))

for document in docs :
    print(document.metadata)

# chain = prompt | model |parser
# result = chain.invoke({'topic' :docs[0].page_content})
# print(result)
# python directory_loader.py