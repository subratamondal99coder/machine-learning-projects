def Add(a,b):
    return(a+b)
def Subtract(a,b):
    return(a-b)
def Multiply(a,b):
    return(a*b)
def Divided(a,b):
    if b == 0:
        return("Cannot divided by zero")
    return(a/b)
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("Add.1")
print("Subtract. 2")
print("Multiplt. 3")
print("Divided. 4")
choice= input("Enter your choice:")
if choice == "1":
    print((Add(a,b)))
elif choice == "2":
    print((Subtract(a,b)))
elif choice == "3":
    print((Multiply(a,b)))
elif choice == "4":
    print((Divided(a,b)))
else:
    print("Invalid choice")


