from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt1 = PromptTemplate(
    template='make a LinkedIn post one line on {topic}',
    input_variables=['topic']
    )

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='make a twitter post one line on {topic}',
    input_variables=['topic']
    )

parallel_chain = RunnableParallel({
    'LinkedIn': RunnableSequence(prompt1,model,parser),
    'twitter' : RunnableSequence(prompt2,model,parser)
})

print(parallel_chain.invoke({'topic' : 'modi'}))

# python runnable_parallel.py