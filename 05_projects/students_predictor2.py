import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Load csv
data= pd.read_csv("students.csv")
# Feature and target
x=data[["Hours"]]
y=data["Marks"]
# Split data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Create and train model
model=LinearRegression()
model.fit(x_train,y_train)
# Accuracy(R2 score)
score=model.score(x_test,y_test)
print("R2 score:", score)
# User input
hours=float(input("Enter study hours:"))
# Predict
new_data=pd.DataFrame({"Hours":[hours]})
prediction=model.predict(new_data)
print("Predicted marks:", prediction[0])
# Visualize
plt.scatter(x,y,label="Actual data")
plt.plot(x,model.predict(x),label="Regression line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Students Marks Prediction")
plt.legend()
plt.grid(True)
plt.show()

