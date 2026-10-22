from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template='write a summary about the following topic \n {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

loader = PyPDFLoader('cricket_test.pdf')


docs = loader.load()

print(type(docs))
print(len(docs))
print((docs[0]))
print((docs[0].metadata))


# chain = prompt | model |parser
# result = chain.invoke({'topic' :docs[0].page_content})
# print(result)

# python pdf_loader.py