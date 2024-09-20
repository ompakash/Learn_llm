from decouple import config
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
SECRET_KEY = config('OPENAI_API_KEY')
LANGCHAIN_TRACING_V2=True
LANGCHAIN_API_KEY = config('LANGCHAIN_API_KEY')
## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(api_key=SECRET_KEY)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# LANGCHAIN_API_KEY="<your-api-key>"
# LANGCHAIN_PROJECT="Learn1"