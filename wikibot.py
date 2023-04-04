import openai
import wikipedia
import os
from dotenv import load_dotenv

load_dotenv()

# Pass the api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get user input
title = input("Title of the page: ")

# Get the wikipedia content
wikipedia.set_lang("es")
page = wikipedia.page(title=title, auto_suggest=False)


# Define prompt
prompt = "Create a 5-bullet point summary of: " + page.content[:10000]
messages = []
messages.append(
    {"role": "user", "content": prompt})

try:
    # make an api
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.8)

    # Print the response
    print(response.choices[0].message.content)
# authentication issue
except openai.error.AuthenticationError as e:
    print('No valid token / auth error')
    print(e)

except openai.error.InvalidRequestError as e:
    print('Invalid request, read the manual')
    print(e)
