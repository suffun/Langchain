from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# ist template
template1 = PromptTemplate(
    template='write a detail report on {topic}',
    input_variables=['topic']

)
template2 = PromptTemplate(
    template='write a five line summary on the following text. /n {text}',
    input_variables=['text']

)

prompt1 = template1.invoke({'topic' : 'eaarth'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result.text})


result2 = model.invoke(prompt2)

print(result2.text)