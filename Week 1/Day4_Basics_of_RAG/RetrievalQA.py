# Using RetrievalQA, create a pipeline that can answer the question: 
# “What is the refund policy?” 
# based on a sample company policy document. 
 

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

embedding_model = OpenAIEmbeddings(api_key="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"
)

loader = TextLoader(r"C:\Users\469461\Desktop\Poorvaja\dataset\CompanyPolicy.txt", encoding='utf-8')

documents = loader.load()

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is the refund policy?"
results = retriever.invoke(query)

print(results)
print(len(results))


# pip install chromadb

# output

# [Document(metadata={'source': 'C:\\Users\\469461\\Desktop\\Poorvaja\\dataset\\'
# 'CompanyPolicy.txt'}, page_content='Company Policy:\n- Refunds are available' \
# ' within 30 days of purchase if the product is defective or not as described.\n- ' \
# 'No refunds after 30 days.\n- Customers must provide proof of purchase to claim ' \
# 'a refund.')]
# 1