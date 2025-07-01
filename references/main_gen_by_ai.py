#!/usr/bin/env python3
import argparse
import requests
import os
from dotenv import load_dotenv

parser = argparse.ArgumentParser(description='Translate sentences using LLM API.')
parser.add_argument('sentence', type=str, help='The sentence to translate.')
parser.add_argument('--from', dest='source_lang', type=str, default='Chinese', help='Source language (default: Chinese)')
parser.add_argument('--to', dest='target_lang', type=str, default='English', help='Target language (default: English)')
args = parser.parse_args()

load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')  
if not api_key:
    print("Error: DEEPSEEK_API_KEY environment variable not set.")
    exit(0)

prompt = f"Translate the following {args.source_lang} text to {args.target_lang}: '{args.sentence}'"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'model': 'deepseek-chat',
    'messages': [
        {'role': 'user', 'content': prompt}
    ]
}

try:
    response = requests.post('https://api.deepseek.com/chat/completions', headers=headers, json=data, timeout=10)
    response.raise_for_status()
    result = response.json()
    translated_text = result['choices'][0]['message']['content']
    print(translated_text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")