import openai, os

openai.organization = ''
openai.api_key = ''
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""
'''’‘’
Medical_Record
Analysis_Case
Case_Info
Case_Info
Predict_Case
Predict_Recommend_Treatment
'''
messages = [
        {"role": "system", "content": "You are a helpful assistant."},
]

prompt = ''
messages.append({"role": "user", "content": prompt})

while True:
    message = input("User: ")
    if message:
        messages.append(
                {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )
    answer = chat_completion.choices[0].message.content
    messages.append({"role": "system", "content": answer})
    print(f"ChatGPT:\n{answer}")

