students = {
    "student1":{
        "name":"alice",
        "age":25,
        "city":"new york"
    },
    "student2":{
        "name":"bob",
        "age":45,
        "city":"kalyan"
        },
    "student3":{
        "name":"leo",
        "age":34,
        "city":"mumbai"
    }
}
print("all keys and values in the nested dictionary:\n")
for student_key,student_info in students.items():
    print(f"{student_key}:")
    for key,value in student_info.items():
        print(f"{key}:{value}")
        print()