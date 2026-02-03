"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert"),
    HumanMessage(content="Explain in simple terms, what is {topic}")
])

prompt = template.invoke({
    "domain": "cricket",
    "topic": "Dusra"
})

print(prompt)
"""

from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Explain in simple terms, what is {topic}")
])

prompt = template.invoke({
    "domain": "cricket",
    "topic": "Dusra"
})

print(prompt)