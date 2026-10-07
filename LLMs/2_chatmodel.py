# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents="What is the capital of India?"
# )

# print("3. Response:")
# print(response.text)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash"
)

response = model.invoke("What is the capital of India?")

print(response)