def Add(a,b):
    return(a+b)
def Subtract(a,b):
    return(a-b)
def Multiply(a,b):
    return(a*b)
def Divided(a,b):
    return(a/b)
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("Add.1")
print("Subtract. 2")
print("Multiplt. 3")
print("Divided. 4")
choice= int(input("Enter your choice"))
if "1":
    print((Add(a,b)))
elif "2":
    print((Subtract(a,b)))
elif "3":
    print((Multiply(a,b)))
elif "4":
    print((Divided(a,b)))


