from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model="gpt-4")
# result = model.invoke("what is the capital of india?")
# print(result)
# print(result.content)

# model = ChatOpenAI(model="gpt-4", temperature=0)
# result = model.invoke("suggest me 5 indian male names")
# print(result.content)

# model = ChatOpenAI(model="gpt-4", temperature=1.8)
# result = model.invoke("suggest me 5 indian male names")
# print(result.content)

# model = ChatOpenAI(model="gpt-4", temperature=0)
# result = model.invoke("write a 5 line poem on cricket")
# print(result.content)

# model = ChatOpenAI(model="gpt-4", temperature=1.5)
# result = model.invoke("write a 5 line poem on cricket")
# print(result.content)

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)
result = model.invoke("write a 5 line poem on cricket")
print(result.content)