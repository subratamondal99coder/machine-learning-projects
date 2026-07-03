from sklearn.linear_model import LinearRegression
import numpy as np
# Hours studied
x=np.array([[2],[4],[6],[8],[10]])
# Marks obtained
y=([20,40,60,80,100])
# Create model
model= LinearRegression()
# Train model
model.fit(x,y)
# Predict marks for 6 hours
prediction=model.predict([[12]])
print("predicted marks:", prediction)