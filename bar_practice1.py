import matplotlib.pyplot as plt
x=["Apple","Banana","Orange","Mango"]
y=[50,30,40,60]
plt.bar(x,y,color=["r","y","orange","g"],width=0.5,edgecolor="black")
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.grid(axis="y")
plt.show()