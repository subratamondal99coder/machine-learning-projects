import matplotlib.pyplot as plt
subjects=["Maths","Physics","Chemistry","Biology"]
marks=[90,85,92,99]
plt.pie(marks,labels=subjects,colors=["r","g","b","purple"],autopct="%1.1f%%",shadow=True,startangle=90)
plt.title("Marks Distribution")
plt.show()
plt.savefig("graph.png")