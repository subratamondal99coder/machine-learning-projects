import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import joblib
# Load data
data=pd.read_csv("05_projects/house_price.csv")
# Feature and target
x=data[["Area","Bedrooms","Age"]]
y=data["Price"]
# Split data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Create and train model
model=LinearRegression()
model.fit(x_train,y_train)
# R2 score
score=model.score(x_test,y_test)
print("R2 score:", score)
# User input
area=float(input("Enter area (sq ft):"))
bedrooms=int(input("Enter number of bedrooms:"))
age=int(input("Enter house age:"))
# Creata dataframe
new_house=pd.DataFrame({"Area":[area], "Bedrooms":[bedrooms], "Age":[age]})
# Predict
prediction=model.predict(new_house)
print("Predicted House Price:", prediction[0])
# Predict test data
y_pred=model.predict(x_test)
# Plot
plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred,label="Predict Vs Actual")
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.title("Actual vs Predicted House Price")
plt.legend()
plt.grid(True)
plt.show()
joblib.dump(model,"house_model.pkl")




