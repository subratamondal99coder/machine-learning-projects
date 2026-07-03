import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[50,60,70,85,95]
plt.scatter(x,y,color="r",s=100)
plt.title("Study Hours Vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()