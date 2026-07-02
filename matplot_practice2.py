import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[20,45,10,34,56]
plt.plot(x,y,"g*:",lw=4,ms=12,mfc="red",mec="black",label="Temperature")
plt.title("Weather report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.legend()
plt.show()