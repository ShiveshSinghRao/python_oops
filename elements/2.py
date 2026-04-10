# DICTIONARY BASICS

person = {
    "name": "Rao",
    "age": 25,
    "city": "Chennai"
}

# Access
print(person["name"])
print(person.get("age"))

# Add / Update
person["age"] = 26
person["job"] = "Engineer"

# Loop keys
for key in person:
    print("Key:", key)

# Loop values
for value in person.values():
    print("Value:", value)

# Loop key-value
for key, value in person.items():
    print(key, "->", value)