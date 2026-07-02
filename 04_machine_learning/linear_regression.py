from sklearn.linear_model import LinearRegression
import numpy as np
# Hours studied
x=np.array([[1],[2],[3],[4],[5]])
# Marks obtained
y=np.array([40,50,60,70,80])
# Create model
model=LinearRegression()
# Train model
model.fit(x,y)
# Predict marks for 6 hours study
prediction=model.predict([[6]])
print("Predicted score:", prediction)


