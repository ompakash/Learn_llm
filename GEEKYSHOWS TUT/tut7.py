from langchain_openai import OpenAIEmbeddings
from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')

embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# text = "this is sample text"
# embedded_query = embeddings_model.embed_query(text)
# print(embedded_query)


texts = [
    "hi how are you",
    "where are you nowdays"
]

embedded_docs = embeddings_model.embed_documents(texts)
print(embedded_docs)