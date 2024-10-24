import json

with open("data.json", "r") as f:
    data = json.load(f)
    for key in data:
        print(key)
    print(data["Facebook"]["password"])