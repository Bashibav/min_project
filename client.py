from openai import OpenAI

client = OpenAI(api_key="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")  # Replace securely, e.g., via environment variable

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use "gpt-4" or "gpt-4o", not "gpt-4.1"
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(completion.choices[0].message.content)
