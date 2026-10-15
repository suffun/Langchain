from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
model2 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
prompt1 = PromptTemplate(
    template = 'generate a short and simple notes on the following  {text}',
    input_variables=['text']

)
prompt2 = PromptTemplate(
    template = 'generate a 5 short questions on the following text  \n  {text}',
    input_variables=['text']

)
prompt3 = PromptTemplate(
    template = 'merge the provided notes and quiz into a single document  \n notes ->  {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']

)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 |model1 | parser,
    'quiz' : prompt2 | model2 |parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """ 
Python is a high-level programming language known for its simple syntax
and readability. It is widely used in web development, data science,
machine learning, automation, and artificial intelligence.
"""


result = chain.invoke({'text' : text})
print(result)

chain.get_graph().print_ascii()

# python parallel_chain.py 