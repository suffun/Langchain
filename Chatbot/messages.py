from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

messages = [
    SystemMessage(content='Yopu are a helpful Assiatant').content,
    HumanMessage(content='what is apple')
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)