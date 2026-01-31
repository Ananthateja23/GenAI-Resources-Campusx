from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Delhi is the capital of India"
result = embedding.embed_query(text)

print(str(result))


# Use for documents embeddings
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(
#     model="sentence-transformers/all-MiniLM-L6-v2"
# )

# documents = [
#     "Delhi is the capital of India",
#     "Bangalore is the capital of Karnataka",
#     "Paris is the capital of France"
# ]
# result = embedding.embed_documents(documents)

# print(str(result))

