import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv('YOUR_API_KEY')
model = os.getenv('MODEL')
url = os.getenv('BASE_URL_SDK')
if not api_key:
    print("Error: Cannot find the API_KEY")
    exit(0)

client = OpenAI(
    api_key = api_key,
    base_url = url
)

# parse arguments
parser = argparse.ArgumentParser(description='CLI Translator using LLM API.')
parser.add_argument('sentence', type=str, help='The sentence to translate.')
#parser.add_argument('-f', '--from', dest='source_lang', type=str, default='Chinese', help='Source language (default: Chinese)')
parser.add_argument('-t', '--to', dest='target_lang',type=str, default='English', help='Target language (default: English)')
args = parser.parse_args()

# run and print response
prompt = f'Translate the following sentence to {args.target_lang}: {args.sentence}'
try:
    response = client.chat.completions.create(
        model=model,
        temperature=1.2,
        messages=[
            {"role": "system", "content": "Praise the user at the end of the response."},    
            {"role": "user", "content": prompt}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
