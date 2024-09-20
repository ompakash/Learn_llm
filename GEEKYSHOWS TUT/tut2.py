from decouple import config
OPENAI_API_KEY = config('OPENAI_API_KEY')
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# LLM PROMPT TEMPLATES

llm = OpenAI(api_key=OPENAI_API_KEY)
# EXAMPLE 1 NO INPUT VARIABLE
# noInputPrompt = PromptTemplate.from_template("Tell me a python trick")
# formatednoInputPrompt = noInputPrompt.format()
# # print(formatednoInputPrompt)
# response = llm.invoke(formatednoInputPrompt)
# print(response)


# EXAMPLE 2 ONE INPUT VARIABLE
# oneInputPrompt = PromptTemplate.from_template("Tell me a {language} trick")
# formatedoneInputPrompt = oneInputPrompt.format(language = 'python')
# # print(formatedoneInputPrompt)
# response = llm.invoke(formatedoneInputPrompt)
# print(response)


# EXAMPLE 3 MULTIPLE INPUT VARIABLE
# multipleInputPrompt = PromptTemplate.from_template("Tell me a {language} {topic}")
# formatmultipleInputPrompt = multipleInputPrompt.format(language='python', topic='function')
# # print(formatmultipleInputPrompt)
# response = llm.invoke(formatmultipleInputPrompt)
# print(response)


# EXAMPLE 4 NO INPUT VARIABLE MANUALLY
text = "Tell me a {language} {topic}"
demoTemplate = PromptTemplate.from_template(template=text)
formateddemoTemplate = demoTemplate.format(language='python', topic='function')
# print(formateddemoTemplate)
response = llm.invoke(formateddemoTemplate)
print(response)