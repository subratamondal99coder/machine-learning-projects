import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[15,35,25,30,45]
plt.plot(x,y,"g*:",lw=5,ms=14,mfc="red",mec="yellow",label="Temperature")
plt.title("Weather report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.legend()
plt.show()