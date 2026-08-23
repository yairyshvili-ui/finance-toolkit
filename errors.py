import json

try:
    with open("missing_file.json") as f:
        data = json.load(f)
    print(data)
except FileNotFoundError:
    print("File not found - using empty list instead")
    data = []

print("Continuing with data:", data)
