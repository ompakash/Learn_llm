from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

chat = ChatOpenAI(api_key=OPENAI_API_KEY)

# EXAMPLE 1
# chatPrompt = ChatPromptTemplate.from_messages(
#     [('system', "you are an expert lingustic you can translate {input_language} to {output_language}"), 
#     ('human', "{text}") ]
# )
# formatedchatPrompt = chatPrompt.format_messages(input_language='english', output_language='hindi', text='hello how are you?')
# # print(formatedchatPrompt)
# response = chat.invoke(formatedchatPrompt)
# print(response)
# print(response.content)


# EXAMPLE 2
# sys_template = "you are an expert lingustic you can translate {input_language} to {output_language}"
# human_template= "{text}"

# chatPrompt = ChatPromptTemplate.from_messages(
#     [SystemMessagePromptTemplate.from_template(sys_template), HumanMessagePromptTemplate.from_template(human_template)])

# formatedchatPrompt = chatPrompt.format_messages(input_language='english', output_language='hindi', text = "hello how are you?")
# # print(formatedchatPrompt)
# response = chat.invoke(formatedchatPrompt)
# print(response)
# print(response.content)

# EXAMPLE 3
sys_prompt = PromptTemplate.from_template("you are an expert lingustic you can translate {input_language} to {output_language}")
human_prompt= PromptTemplate.from_template("{text}.")

sys_msg_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)
human_msg_prompt = HumanMessagePromptTemplate(prompt=human_prompt)

chatPrompt = ChatPromptTemplate.from_messages([sys_msg_prompt, human_msg_prompt])
formatedchatPrompt = chatPrompt.format_messages(input_language='english', output_language='hindi', text= "hello how are you?")

# print(formatedchatPrompt)
response = chat.invoke(formatedchatPrompt)
print("Response = ", response)
print("CONTENT =  ", response.content)