'''
# chatbot without chathistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini-2024-07-18")

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)

'''

'''
# chatbot with chathistory but unaware of personality

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini-2024-07-18")
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)

'''

# chatbot with chathistory and personlity aware
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini-2024-07-18")
chat_history = [
    SystemMessage(content = "You are a helpful assisstant")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)
