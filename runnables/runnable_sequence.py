from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
    )

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='explain the following joke bro {text}',
    input_variables=['text']
    )

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({'topic' : 'modi'}))

# python runnable_sequence.py