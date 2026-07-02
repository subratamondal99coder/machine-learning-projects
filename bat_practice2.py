import matplotlib.pyplot as plt
x=["Math","Physics","Chemistry","Biology"]
y=[95,88,90,85]
plt.barh(x,y,color=["b","g","r","purple"],height=0.6,edgecolor="black")
plt.title("Exam Marks(Horizontal)")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.grid(axis="x")
plt.show()