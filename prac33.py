my_dict ={
    "apple":10,
    "banana":20,
    "cherry":15
}
total = sum(my_dict.values())

print("sum of dictionary: ",total)
#sum only numeric values in a dictionary
print("only numeric values in a dictionary")

y_dict = {
    "apple ":10,
    "banana":"yellow",
    "cherry":15,
    "price":5.5,
    "note":"fruit"
}
total = 0
for value in y_dict.values():
    if isinstance(value,(int,float)):
        total += value
print("the sum of all numeric value is :",total)