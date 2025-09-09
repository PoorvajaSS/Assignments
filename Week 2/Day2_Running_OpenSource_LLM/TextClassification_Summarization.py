# Create a Python virtual environment and install transformers and torch. Pick a 
# small open-source model (like distilbert-base-uncased). Load the model and 
# tokenizer in Python. Use it to perform a simple task (e.g., text classification,
#  summarization). using hugging face can u help me to solve this


from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text = """What is RAG?

RAG (Retrieval-Augmented Generation) is a technique that combines retrieval (searching for information) with generation (creating text with a language model).

Instead of relying only on the model’s internal knowledge, RAG allows the model to look up external documents or databases and then use that information to give more accurate, up-to-date, and factual answers.

Why is RAG Needed?

LLMs (like GPT, BERT, etc.) are trained on fixed data and can’t always handle new information.

They sometimes hallucinate (make up facts).

RAG reduces hallucinations and improves reliability by grounding answers in real documents.

How RAG Works (Steps)

User Question (Query)
→ e.g., “What is the refund policy of Company X?”

Retriever (Search Engine / Vector Database)

Converts the question into an embedding (vector form).

Looks up relevant documents from an external knowledge base (PDFs, company docs, websites, etc.).

Augmentation (Context Injection)

Retrieved documents are added to the user’s question.

Example:

Context: Company X offers refunds within 30 days if products are unused.
Question: What is the refund policy?

Generator (LLM)

The model uses both the question + retrieved context to generate an answer.

Output: “The refund policy allows returns within 30 days if items are unused.”

RAG Architecture (Simple View)
User Query → Retriever → Relevant Docs → Augment Query + Docs → Generator (LLM) → Final Answer

Example in Real Life
Chatbots for customer service: Instead of memorizing every company policy, the bot retrieves policies from a database.

Healthcare apps: Retrieve latest medical research before answering.

Finance apps: Use RAG to answer questions based on up-to-date financial reports.

Benefits of RAG
Provides up-to-date and factual answers
Reduces hallucinations
Handles domain-specific knowledge (company docs, manuals, etc.)
More efficient than retraining a model"""

summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

print(summary[0]['summary_text'])

# environment creation 

#  python -m venv venv 
# venv\Scripts\Activate

# pip install torch transformers

# output

# """ RAG (Retrieval-Augmented Generation) combines retrieval (searching for 
# information) with generation (creating text with a language model) Instead
# of relying only on the model’s internal knowledge, RAG allows the model to 
# look up external documents and then use that."""

