from openai import OpenAI
import sys
client = OpenAI()

resources = """Resources from 2nd Year, 2nd Semester
Syllabus - 1Eb7b2CQld4TMW9PuMEwOuqv3FRVWKpVe
P&S Notes U1 - 1ncLLOKH0M4YPHsK7NKSErCfZxBEYf6h2
P&S Notes U2 - 1nhUa1jERDTeBy6P9OOSA_s06BCHDhul5
DBMS Notes U1 - 1niTogaVsUK7cb_AmijPv2xny3YOTPf6r
DBMS Notes U2 - 1niTogaVsUK7cb_AmijPv2xny3YOTPf6r
MEFA Notes U1 - 1oVJkj_H9e9z_GwYKN-QDZwaxOuiZ17Mo
MEFA Notes U2 - 1oW3VTQUTlx6UCU8EKJnwhHZgTL6zD4Iw
OS Notes U1 - 1nVZmPLaFdsMnDdibR142dpKvEAz5lVly
OS Notes U2 - 1nZ_o2cclL2iu6N8-afiBylVoWDpahuYc
SE Notes U1 - 1od5yuQeix23JSFT6fB-4TDmwIQLFiIGd
SE Notes U2 - 1oe8bHfiuyPIKkH6Gyc1hWP4Orv0M5jUp
P&S Assignment 1 - 1mJlMaMDxUHVqpvIHMDwcJ7MroKyMFJH4
P&S Assignment 2 - 1mJq2yy2LKmE2bW6N_VAVGgMQVAOWsoXf
DBMS Assignment 1 - 1mMcEuIiz5MG4aXUX3Yp0-uVVZ5i7-687
DBMS Assignment 2 -
MEFA Assignment 1 - 1ma3FQU3KUMp8s9RVUOXsdklkgYnLO_w4
MEFA Assignment 2 - 1mroT1bJrzHkiHQIf9hFz-A7kPavaaUKW
OS Assignment 1 - 1muEPWSyo80JaKUOCssKPXbTC9TVlP180
OS Assignment 2 - 1myLJf3jFXtcg9GzUhNj4WhdVSlDZTkbJ
SE Assignment 1 - 1ud5bkxRpSESSIz6rzajOx4GqtbeXR9z2
SE Assignment 2 - 1ukbUwFj7bv0xeNdHZ4lT2NkptgprQBF4"""

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
print(completion.choices[0].message.content)