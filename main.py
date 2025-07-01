import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('YOUR_API_KEY')
model = os.getenv('MODEL')
url = os.getenv('BASE_URL')
if not api_key:
    print("Error: Cannot find the API_KEY")
    exit(0)

parser = argparse.ArgumentParser(description='CLI Translator using LLM API.')
parser.add_argument('sentence', type=str, help='The sentence to translate.')
#parser.add_argument('-f', '--from', dest='source_lang', type=str, default='Chinese', help='Source language (default: Chinese)')
parser.add_argument('-t', '--to', dest='target_lang',type=str, default='English', help='Target language (default: English)')
args = parser.parse_args()

prompt = f'Translate the following sentence to {args.target_lang}: {args.sentence}'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
data = {
    'model': model,
    'messages': [{'role': 'user', 'content': prompt}],
    'temperature': 1.1
}

try:
    response = requests.post(url, headers=headers, json=data, timeout=10)
    response.raise_for_status()
    result = response.json()
    print(result['choices'][0]['message']['content'])
except requests.exceptions.RequestException as e:
    print (f'Error: {e}')