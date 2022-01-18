import json

nums = [12, 2, 4, 89]
fname = 'data.json'
with open(fname, 'w') as f:
    json.dump(nums, f)
