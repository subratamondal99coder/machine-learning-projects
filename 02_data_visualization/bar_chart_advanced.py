import matplotlib.pyplot as plt
x=["Rahul","Priya","Amit","Neha"]
y=[80,92,75,88]
plt.barh(x,y,color=["g","r","purple","orange"],height=0.6,edgecolor="yellow")
plt.title("Students Marks(Horizental)")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.grid(axis="x")
plt.show()