print("1) addition")
print("2) subtraction")
print("3) multiplacation")
print("4) division")

choice = input("Choose an option >> ")

if choice == "1" :
    x = input("Enter number: ")
    y = input("Enter number: ")
    x = int(x) 
    y = int(y)
    print ("The sum of", x,"and", y, "is", x + y )
elif choice == "2" :
    x = input("Enter number: ")
    y = input("Enter number: ")
    x = int(x) 
    y = int(y)
    print ("The difference of", x,"and", y, "is", x - y )
elif choice == "3":
    x = input("Enter number: ")
    y = input("Enter number: ")
    x = int(x) 
    y = int(y)
    print ("The product of", x,"and", y, "is", x * y )
elif choice == "4":
    x = input("Enter number: ")
    y = input("Enter number: ")
    x = int(x) 
    y = int(y)
    if x % y == 0 : 
        answer = x/y 
        print ("The sum of", x,"and", y, "is", int(answer) )
    else : print("Irrational number")
else : print("Incorrect choice")
