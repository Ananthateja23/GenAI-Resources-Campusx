from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# meta-llama/Llama-3.1-8B-Instruct 
# Qwen/Qwen2.5-7B-Instruct
# TinyLlama/TinyLlama-1.1B-Chat-v1.0
llm = HuggingFaceEndpoint(
repo_id="Qwen/Qwen2.5-7B-Instruct",
task="text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("what is the capital of india")

print(result.content)