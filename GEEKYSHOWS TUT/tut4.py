from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.output_parsers import DatetimeOutputParser, CommaSeparatedListOutputParser, PydanticOutputParser

chat = ChatOpenAI(api_key=OPENAI_API_KEY)

date_time_parser = DatetimeOutputParser()
# print(date_time_parser.get_format_instructions())

# comma_sep_parser = CommaSeparatedListOutputParser()
# print(comma_sep_parser.get_format_instructions())


# human_template = "{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(human_template)])
# formated_chatprompt = chat_prompt.format_messages(request = "when world war 2 declared?",format_instruction=date_time_parser.get_format_instructions() )
# # print(formated_chatprompt)
# response = chat.invoke(formated_chatprompt)
# print("RESPONSE", response.content)
# print("RESPONSE CONTENT PARSER ", date_time_parser.parse(response.content))

