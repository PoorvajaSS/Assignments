# few shot prompt


from langchain_openai import OpenAI

llm = OpenAI(
             model="gpt-3.5-turbo-instruct",
             temperature=0 , 
             api_key="sk-proj-vP2nT_o._W-EB3HWF-wcmniXqLSlemkVLMgVgyh3Of_tnMNuBD3XMc30KFa7tjZSS54LZZv16xT3BlBkFJQKFxmMQB952yFLwpJC6I10I-7hAIUBfsg_ApRvTjR9bWp2a3rQVeabZk67LF0i451p4Q8A"
)

while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = llm.invoke(user_input)
    print("AI:", response)