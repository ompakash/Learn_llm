from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


# llm = OpenAI(api_key=OPENAI_API_KEY)
# response = llm.invoke('How many hours in a week?')
# print(response)


# chat = ChatOpenAI(api_key=OPENAI_API_KEY)
# response = chat.invoke("Hi where do you live")
# print(response)
# print(response.content)

chat = ChatOpenAI(api_key=OPENAI_API_KEY)
message = [
    SystemMessage(content='You are a expert developer'),
    HumanMessage(content='what is python ')
]
response = chat.invoke(message)
print(response)
print(response.content)