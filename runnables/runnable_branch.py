from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='write  a detail report  on {topic}',
    input_variables=['topic']
    )
prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
    )

parser = StrOutputParser()



repoort_gen_chain = RunnableSequence(prompt1,model,parser);

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(repoort_gen_chain,branch_chain)

print(final_chain.invoke({'topic' : 'modi'}))

# python runnable_branch.py