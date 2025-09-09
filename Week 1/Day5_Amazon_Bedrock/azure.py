from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="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",
    api_version="2024-02-01",
    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com/"
)

response = client.chat.completions.create(
    model="gpt-35-turbo",   # Azure model deployment name
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain Azure OpenAI in simple terms"}
    ]
)

print(response.choices[0].message.content)


# output 

# Azure OpenAI is a service from Microsoft that lets you use powerful AI models (like GPT) in your own apps. 
# It works through the Azure cloud, so you get security, scalability, and integration with other Azure services. 
# In simple terms, it allows businesses and developers to add advanced AI features like chatbots, summarization, 
# and text analysis into their applications easily.
