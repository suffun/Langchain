# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = OpenAI( model="gpt-5-mini")

# result = llm.invoke("WHat is the capital of india")
# print(result)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    timeout=30,
)

result = llm.invoke("What is the capital of India?")
print(result.content)