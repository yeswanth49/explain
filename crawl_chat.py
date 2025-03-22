from openai import OpenAI
from bs4 import BeautifulSoup
import requests
import sys
client = OpenAI()

url ="https://pecup.in"
response = requests.get(url)

resources = BeautifulSoup(response.text,'html.parser')

question = sys.argv[1]

content = f"{resources}\nQuestion: {question}"

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. that provides resources to students. add prefix https://drive.google.com/file/d/+file_id+/view"},
        {
            "role": "user",
            "content": content
        }
    ],
    max_tokens=100
)
print(completion.usage)
print(content)
print(completion.choices[0].message.content)