import matplotlib.pyplot as plt
subjects=["Math","Physics","Chemistry","Biology"]
marks=[95,88,90,85]
plt.pie(marks,labels=subjects,colors=["b","g","r","purple"],autopct="%1.1f%%")
plt.title("Maks Distrubution")
plt.show()