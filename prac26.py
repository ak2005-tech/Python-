
my_dict = {
    "name": "alice",
    "age": 25,
    "city": "new york"
}
print("Values in the dictionary")
for value in my_dict.values():
    print(value)
print()

people = [
    {"name": "alice", "age": 25, "city": "new york"},
    {"name": "bob", "age": 21, "city": "kalyan"},
    {"name": "lisa", "age": 35, "city": "mumbai"}
]

for person in people:
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print()


# 3. Dictionary with numbered keys

student = {
    1: {"name": "alice", "age": 25, "city": "new york"},
    2: {"name": "anshu", "age": 12, "city": "pune"},
    3: {"name": "raj", "age": 34, "city": "delhi"}
}

for key in student:
    print("Person:", key)
    print("Name:", student[key]["name"])
    print("Age:", student[key]["age"])
    print("City:", student[key]["city"])
    print()