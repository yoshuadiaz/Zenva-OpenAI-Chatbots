import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Pass the api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define prompt
messages = []
messages.append(
    {"role": "system", "content": "You are a CTO mentoring developers. dont't only provide answers also ask guiding questions. And you speak Spanish perfectly."})
messages.append(
    {"role": "user", "content": "Hola, qué debería aprender sobre IA para crear valor en la empresa usando las soluciones de openai y huggingface?"})

try:
    # make an api
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.8, n=2, max_tokens=250)

    # Print the response
    print(response.choices[0].message.content)
# authentication issue
except openai.error.AuthenticationError:
    print('No valid token / auth error')

except openai.error.InvalidRequestError:
    print('Invalid request, read the manual')
