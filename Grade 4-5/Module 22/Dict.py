# Sample dictionary with initial data
person = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "painting", "cycling"],
    "city": "New York"
}

# Displaying the dictionary
print("Initial Dictionary:")
print(person)

# Accessing dictionary elements
print("\nAccessing Elements:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Hobbies: {', '.join(person['hobbies'])}")
print(f"City: {person['city']}")

# Adding a new key-value pair
person["profession"] = "Software Engineer"
print("\nDictionary after adding a new key-value pair:")
print(person)

# Updating an existing value
person["city"] = "San Francisco"
print("\nDictionary after updating the city:")
print(person)

# Removing a key-value pair
del person["age"]
print("\nDictionary after removing the 'age' key:")
print(person)

# Looping through keys and values
print("\nLooping through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
key_to_check = "hobbies"
if key_to_check in person:
    print(f"\n'{key_to_check}' exists in the dictionary. Value: {person[key_to_check]}")
else:
    print(f"\n'{key_to_check}' does not exist in the dictionary.")

# Clearing the dictionary
person.clear()
print("\nDictionary after clearing all entries:")
print(person)
