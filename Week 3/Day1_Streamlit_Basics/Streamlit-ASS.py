from langchain_openai import ChatOpenAI

import streamlit as st

model = ChatOpenAI(api_key="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"
)

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

if st.button('Summarize'):
    st.write("Hello")

# url --> http://localhost:8501/