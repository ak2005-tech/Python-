import my_math

def menu():
      print("\n----Simple Calculator---")
      print ("1.Add")
      print ("2.Subtract")
      print ("3.Multiply")
      print ("4.Divide")
      print ("5.Exit")

while True:
      menu()
      choice = input("Enter your choice (1-5):")

      if choice in['1','2','3','4']:
            try:
                  a=float(input("Enter first number:"))
                  b=float(input("Enter second number:"))

                  if choice=='1':
                      print("Result",my_math.add(a,b))
                  elif choice=='2':
                      print("Result",my_math.subtract(a,b))
                  elif choice=='3':
                      print("Result",my_math.multiply(a,b))
                  elif choice=='4':
                       result= my_math.division(a,b)
                       print("Result:", result)
            except ValueError:
                        print("Invalid input! Please enter numeric values")
      else:
                print("Invalid choice, Please enter a number 1-5")
