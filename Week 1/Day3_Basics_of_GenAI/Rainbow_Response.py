# 1)Write a Python script to send a prompt "Explain how rainbows are formed" 
# using OpenAI’s GPT-3.5 Turbo or Hugging Face Transformers and print the 
# response. 


from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
             model="gpt-3.5-turbo-instruct",
             temperature=0 , 
             api_key="sk-proj-vP2nT_o._W-EB3HWF-wcmniXqLSlemkVLMgVgyh3Of_tnMNuBD3XMc30KFa7tjZSS54LZZv16xT3BlBkFJQKFxmMQB952yFLwpJC6I10I-7hAIUBfsg_ApRvTjR9bWp2a3rQVeabZk67LF0i451p4Q8A"
)

result = llm.invoke("Explain how rainbows are formed")

print(result)
