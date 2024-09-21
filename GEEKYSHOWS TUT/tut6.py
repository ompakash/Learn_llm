from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, Language

# with open("./data/sample3.txt") as f:
#     sample_data = f.read()
# text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=200)
# my_data = text_splitter.create_documents([sample_data])
# print(my_data[0].page_content)



PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)