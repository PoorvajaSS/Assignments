# 2) Create a chain-of-thought prompt: 


# Assignment 2: Role-based & Chain-of-Thought Prompting 

# Objective: Learn role-based and step-by-step reasoning prompts. 
    
# Instructions: 

# Choose a task like “Explain how photosynthesis works.” 

# Create a role-based prompt: 
# “You are a high school biology teacher. Explain photosynthesis to students in simple words.” 

# Create a chain-of-thought prompt: 
# “Explain photosynthesis step by step, reasoning each step clearly.” 

# Test both prompts and observe the difference in response detail and clarity. 

# Deliverables: A table with prompts, model outputs, and short reflections.

from langchain_openai import OpenAI

llm = OpenAI(
             model="gpt-3.5-turbo-instruct",
             temperature=0 , 
             api_key="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"
)

while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = llm.invoke(user_input)
    print("AI:", response)