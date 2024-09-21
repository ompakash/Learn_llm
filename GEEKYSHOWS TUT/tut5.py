from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_community.document_loaders import TextLoader,CSVLoader, BSHTMLLoader, PyPDFLoader
chat = ChatOpenAI(api_key=OPENAI_API_KEY)

# EXAMPLE 1 TEXT FILE
# loader = TextLoader("./data/sample3.txt")
# mydata = loader.load()
# # print(mydata[0].page_content)
# print(mydata[0].metadata)


# EXAMPLE 2 CSV FILE
# loader = CSVLoader("./data/loan.csv")
# mydata = loader.load()
# # print(mydata[0].page_content)
# print(mydata[0].metadata)


# EXAMPLE 3 HTML FILE
# loader = BSHTMLLoader("./data/sample1.html")
# mydata = loader.load()
# print(mydata[0].page_content.replace('\n',' '))
# print(mydata[0].metadata)


# EXAMPLE 4 PDF FILE
# loader = PyPDFLoader("./data/invoicesample.pdf")
# mydata = loader.load()
# # print(mydata[0].page_content)
# print(mydata[0].metadata)


# EXAMPLE 5 
loader = PyPDFLoader("./data/OM PRAKASH.pdf")
mydata = loader.load()[0].page_content
# print(mydata[0].page_content)
human_content = "{question} \n {candidate_data}"
chat_prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(human_content)])
formated_chat_prompt = chat_prompt.format_messages(
    question="did he have knowledge about machine learning ?",
    candidate_data=mydata
)
# print(formated_chat_prompt)
response = chat.invoke(formated_chat_prompt)
print(response.content)