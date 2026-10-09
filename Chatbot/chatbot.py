
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()

# ___________________________________________________________________________________
import logging
class _SkipAFCWarning(logging.Filter):
    def filter(self, record):
        return "automatic function calling" not in record.getMessage().lower()

logging.getLogger("google_genai.models").addFilter(_SkipAFCWarning())
# ____________________________________________________________________________________

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

chat_history = [
    SystemMessage(content="You Are a Helpful AI Assistant")
]
while True :
    user_input = input('You :')
    chat_history.append(HumanMessage(content=user_input) )
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print('AI :' ,result.text)

print(' this is your history',chat_history)
