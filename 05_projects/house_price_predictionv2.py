import pandas as pd
import joblib
# Load saved model
model=joblib.load("house_model.pkl")
# User input
area=float(input("Enter area:"))
bedrooms=float(input("Enter bedrooms:"))
age=float(input("Enter house age:"))
new_house=pd.DataFrame({"Area":[area],"Bedrooms":[bedrooms],"Age":[age]})
prediction=model.predict(new_house)
print("Predicted house:", prediction[0])

                        