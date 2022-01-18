import json

fname = 'data.json'
with open(fname, 'r') as f:
    content = json.load(f)
print(content)
