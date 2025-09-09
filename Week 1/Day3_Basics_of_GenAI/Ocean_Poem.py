# 2) Use the transformers library from Hugging Face to load a model and
#  generate text from a prompt:  "Write a small poem about the ocean". 
# Print the result. 

from transformers import pipeline

generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

prompt = "Write a small poem about the ocean"

result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])