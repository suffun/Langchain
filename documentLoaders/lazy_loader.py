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

docs = loader.lazy_load()


print((docs))

# print((docs[0].metadata))

for document in docs :
    print(document.metadata)

#  python lazy_loader.py

# lazy loader is faster as compare to loader. we will use lazy loader when data is very large and multipole data files and pdf needed