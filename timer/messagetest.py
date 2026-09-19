import json

with open ("messages.json", 'r') as f:
    messages = json.loads(f.read())

print messages
