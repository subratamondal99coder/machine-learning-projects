import pandas as pd
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import os
import joblib
# Load data
Base_Dir=os.path.dirname(os.path.abspath(__file__))
data=pd.read_csv(os.path.join(Base_Dir,"students_score_multi.csv"))
# Feature and taeget
x=data[["Hours","Sleep","Attendance"]]
y=data["Marks"]
# Split data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Create and train model
model=LinearRegression()
model.fit(x_train,y_train)
# Accuracy(R2 score)
r2=model.score(x_test,y_test)
print("R2 score:", r2)
# User input
hours=float(input("Enter study hours:"))
sleep=float(input("Enter sleep hours:"))
attendance=float(input("Enter attendance percentage:"))
# New data
new_data=pd.DataFrame({"Hours":[hours],"Sleep":[sleep],"Attendance":[attendance]})
# Prediction
prediction=model.predict(new_data)
print("Predicted marks:", prediction[0])
# 3D Visualization
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(data["Hours"],data["Sleep"],data["Marks"])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Sleep Hours")
ax.set_zlabel("Marks")
plt.title("Multiple Linear Regression Data")
plt.show()
# Save model with joblib
joblib.dump(model,os.path.join(Base_Dir,"students_model_v3.pkl"))
