import json

fan_config = {"name": "fanControl",
"FAN_ON": True,
"FAN_SPEED": 70
}

with open("fanConf.json","w") as json_file:json.dump(fan_config, json_file)
