import json

# data = {
#     "name": "Mohit Kumar",
#     "age": 25,
#     "languages": ["Python", "JavaScript", "C++"],
#     "is_trainer": True,
# }

# json_data = json.dumps(data)
# print(json_data)


# json_data = '{"name": "Mohit Kumar", "age": 25, "languages": ["Python", "JavaScript", "C++"], "is_trainer": true}'
# python_data = json.loads(json_data)
# print(python_data)
# print(python_data["name"])
# print(python_data["age"])


data = {
    "name": "Mohit Kumar","age": 25,"languages": ["Python", "JavaScript", "C++"],"is_trainer": True,
}

# with open("student.json", "w") as file:
#     json.dump(data, file)
# print("Data written to student.json")

# with open("student.json", "r") as file:
#     loaded_data = json.load(file)
# print("Data loaded from student.json:", loaded_data)
# print("Name:", loaded_data["name"])

print(json.dumps(data, indent="\t"))  # Pretty print JSON data
