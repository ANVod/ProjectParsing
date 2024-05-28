import json

with open('lightings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    print(item)
    