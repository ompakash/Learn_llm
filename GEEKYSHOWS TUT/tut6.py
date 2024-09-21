from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_community.document_loaders import TextLoader,CSVLoader, BSHTMLLoader, PyPDFLoader
chat = ChatOpenAI(api_key=OPENAI_API_KEY)
