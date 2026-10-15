from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()


class Feedback(BaseModel) :
    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template = 'classify the sentiment of the following feedback text into positive and negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction' : parser2.get_format_instructions()}

)


classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='write appropriate response for this positive feedback {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='write appropriate response for this negative feedback {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiments")
)

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback' : 'i do not like cake'})
print(result)


chain.get_graph().print_ascii()

# python conditional_chain.py