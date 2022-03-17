import json

import json

with open('fanConf.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
print(data["FAN_SPEED"])