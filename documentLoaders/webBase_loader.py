from langchain_community.document_loaders import TextLoader,WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template='Answwer the following question \n {ques} from the following text {text}',
    input_variables=['ques','text']
)

parser = StrOutputParser()

url = 'https://substack.com/@karinadatascientist/note/c-275048626?utmSource=%2Fsearch%2Fpython'

loader = WebBaseLoader(url)

docs = loader.load()

# print(type(docs))
# print(len(docs))
# print((docs[0]))

chain = prompt | model |parser
result = chain.invoke({'ques' : "on which language she is talking about",'text' :docs[0].page_content})
print(result)
# python webBase_loader.py