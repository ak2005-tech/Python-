items = ["apple",123,"banana","orange",45,"grape",7.8,"melon"]
string_count= 0

for item in items:
    if type(item)==str:
        string_count += 1

print("string count :",string_count)