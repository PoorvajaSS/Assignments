from langchain_openai import ChatOpenAI

import streamlit as st

model = ChatOpenAI(api_key="sk-proj-vP2nT_o._W-EB3HWF-wcmniXqLSlemkVLMgVgyh3Of_tnMNuBD3XMc30KFa7tjZSS54LZZv16xT3BlBkFJQKFxmMQB952yFLwpJC6I10I-7hAIUBfsg_ApRvTjR9bWp2a3rQVeabZk67LF0i451p4Q8A"
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
