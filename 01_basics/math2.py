def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divided(a,b):
    if b == 0 :
        return "cannot divided by zero"
    return (a/b)
a=float(input("enter first number"))
b=float(input("enter second number"))
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divided")
choice=input("enter choice:")
if choice == "1":
    print(add(a,b))
elif choice == "2":
    print(subtract(a,b))
elif choice == "3":  
    print(multiply(a,b)) 
elif choice == "4":
    print(divided(a,b))
else:
    print("invalid choice")