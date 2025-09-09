# Assignment 1: Zero-shot vs Few-shot Prompting 

# Objective: Understand the difference between zero-shot and few-shot prompting. 

# Instructions: 

# Pick a simple task (e.g., sentiment analysis of a sentence). 

# Write a zero-shot prompt and test it using any LLM (OpenAI GPT or Hugging Face hosted models). 
# Example: 
# “Determine if the following sentence is positive or negative: ‘I love my new phone.’” 
# Write a few-shot prompt by giving 2–3 examples before the query. 
# Example: 
# mathematica 
# CopyEdit 
# Example 1: "I am happy today." → Positive 
# Example 2: "I am sad today." → Negative 
# Now classify: "The movie was amazing." 
# Compare the outputs and note differences in accuracy. 
# Deliverables: A short report (1–2 pages) with prompts, outputs, and observations. 

#zero shot prompt 

from langchain_openai import OpenAI

llm = OpenAI(
             model="gpt-3.5-turbo-instruct",
             temperature=0 , 
             api_key="sk-proj-vP2nT_o._W-EB3HWF-wcmniXqLSlemkVLMgVgyh3Of_tnMNuBD3XMc30KFa7tjZSS54LZZv16xT3BlBkFJQKFxmMQB952yFLwpJC6I10I-7hAIUBfsg_ApRvTjR9bWp2a3rQVeabZk67LF0i451p4Q8A")
user_input = input('Enter your prompt')

result = llm.invoke(user_input)

print(result)