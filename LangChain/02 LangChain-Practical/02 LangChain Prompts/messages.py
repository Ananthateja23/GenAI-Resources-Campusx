from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini-2024-07-18")
messages = [
    SystemMessage(content="You are a helpful AI assisstant"),
    HumanMessage(content="Tell me about LangChain")
]
result = model.invoke(messages) 
messages.append(AIMessage(content=result.content))

print(messages)