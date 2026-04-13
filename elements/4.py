import json

# JSON string
data = '{"name": "Rao", "age": 25, "skills": ["Python", "JS"]}'

# Convert JSON -> Python dict
parsed = json.loads(data)

print(parsed["name"])
print(parsed["skills"][0])

# Modify
parsed["age"] = 26

# Convert back to JSON 
json_data = json.dumps(parsed, indent=2)

print(json_data)