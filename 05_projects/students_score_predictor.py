import pandas as pd
from sklearn.linear_model import LinearRegression
# Load csv file
data=pd.read_csv("students.csv")
# Feature and target
x=data[["Hours"]]
y=data["Marks"]
# Create and train model
model=LinearRegression()
model.fit(x,y)
# User input
hours=float(input("Enter study hours:"))
# Predict
new_data=pd.DataFrame({"Hours":[hours]})
prediction=model.predict(new_data)
print("Predicted marks:", prediction[0])

