# Load a .txt or .pdf file using LangChain’s TextLoader and split it using 
# RecursiveCharacterTextSplitter. Print the total number of document chunks created. 

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\469461\Downloads\cricket.txt", encoding='utf-8')

docs = loader.load()

print(len(docs))

text = docs[0].page_content

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)

# the total number of document chunks created  --> 27