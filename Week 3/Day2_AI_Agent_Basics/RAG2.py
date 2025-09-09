# Task: Simple Multi-Agent RAG System
# Objective:
# Build a small LangChain multi-agent system where two agents use the same vector store (RAG) but specialize in different topics.
# Stages
# 1 Prepare Data
# --> Create a short text file (or two). Example:
# --> salary.txt: explains how salaries are structured (monthly, annual, deductions).
# --> insurance.txt: explains insurance benefits (coverage, premium, claim process).
# --> Load both into a vector store of your choice

# 2 Agents
# --> Salary Agent: answers only salary-related questions using RAG.
# --> Insurance Agent: answers only insurance-related questions using RAG.
# --> Coordinator Agent: receives a query and decides which agent to call.

# 3 Workflow
# --> User asks: “What is included in my insurance policy?”
# --> Coordinator forwards to Insurance Agent.
# --> Insurance Agent retrieves context from vector store and responds.
# --> Coordinator sends final answer back to the user.

# 4 Deliverables
# --> One Python script.
# --> At least two user queries:
# --> Salary question → handled by Salary Agent.
# --> Insurance question → handled by Insurance Agent.

# Example Query & Output
# Input: “How do I calculate annual salary?”
# Output: “Your annual salary is monthly salary × 12, minus deductions.”


from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_core.runnables import RunnableLambda

salary_loader = TextLoader("salary.txt")
salary_docs = salary_loader.load()

insurance_loader = TextLoader("insurance.txt")
insurance_docs = insurance_loader.load()

all_docs = salary_docs + insurance_docs

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=0,
)

salary_chunks = splitter.split_documents(salary_docs)
insurance_chunks = splitter.split_documents(insurance_docs)
all_chunks = splitter.split_documents(all_docs)

embeddings = OpenAIEmbeddings(
    api_key="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"
)

vectorstore = FAISS.from_documents(all_chunks, embeddings)

llm = ChatOpenAI(
    model="gpt-3.5-turbo", 
    temperature=0,
    api_key="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"
)

salary_qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    chain_type="stuff"
)

insurance_qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    chain_type="stuff"
)

def coordinator(query):
    if "salary" in query.lower() or "annual" in query.lower() or "monthly" in query.lower():
        print("Coordinator chose Salary Agent")
        return salary_qa.run(query)
    elif "insurance" in query.lower() or "policy" in query.lower() or "claim" in query.lower():
        print("Coordinator chose Insurance Agent")
        return insurance_qa.run(query)
    else:
        return "Sorry, I don't know which agent should handle this question."

coordinator_runnable = RunnableLambda(lambda query: coordinator(query))

queries = [
    "How do I calculate annual salary?",
    "What is included in my insurance policy?"
]

for q in queries:
    print(f"\nQ: {q}")
    print("Answer:", coordinator_runnable.invoke(q))


# output 
# Q: How do I calculate annual salary?
# Coordinator chose Salary Agent
# c:\Users\469461\Desktop\VS projects\RAG2.py:84: LangChainDeprecationWarning: The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
#   return salary_qa.run(query)
# Answer: To calculate annual salary, you need to multiply the monthly salary by 12.

# Q: What is included in my insurance policy?
# Coordinator chose Insurance Agent
# Answer: Your insurance policy includes coverage for health, dental, and vision.