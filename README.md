# OpenAI Chatbot and Wikipedia Summarization
This project utilizes OpenAI to create a Spanish language chatbot and summarize Wikipedia content using the OpenAI API and the Wikipedia library.

## Requirements
- Python 3.x
- OpenAI API key
- Python libraries: openai, dotenv, wikipedia

## Setup
1. Clone the repository
2. Install the dependencies: `pip install -r requirements.txt`
3. Copy the `.env.example` file and rename it to `.env`.
4. Obtain an OpenAI API key and paste it into the `.env` file.

## Usage
**OpenAI Chatbot**
1. Run the chatbot.py file with python chatbot.py.
2. The chatbot will prompt for a Spanish language input message.
3. The chatbot will respond with a GPT-3 generated response.

**Wikipedia Summarization**
1. Run the wikibot.py file with python wikibot.py.
2. Enter the title of a Spanish language Wikipedia page.
3. The program will print a 5 bullet point summary of the page.