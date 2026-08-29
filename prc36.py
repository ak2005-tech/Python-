def print_string(s):
    # if the string is empty , stop
    if s=="":
        
     return 
    print(s[0], end ="")
# use end="" to print on the same line
    print_string(s[1:])

user_input = input("Enter a string:")
print("String printed using recursion:")
print_string(user_input)
