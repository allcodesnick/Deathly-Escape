import json

with open('prompts.json') as f:
    data = json.load(f)

for prompt in data['Prompts']:
    print(prompt)