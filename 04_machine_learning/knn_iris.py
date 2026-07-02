from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Load datasets
iris= load_iris()
x= iris.data
y= iris.target
# Split datasets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Create model
model= KNeighborsClassifier(n_neighbors=3)
# Train model
model.fit(x_train,y_train)
# Predict one flower
prediction= model.predict([[5.1,3.5,1.4,0.2]])
print("Predicted class:", prediction)
print("Flower name:",iris.target_names[prediction[0]])
# Check accuracy
accuracy=model.score(x_test,y_test)
print("Accuracy:", accuracy)