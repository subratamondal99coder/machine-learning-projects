from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris= load_iris()
x=iris.data
y=iris.target
print("x shape:", x.shape)
print("y shape:", y.shape)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("/nTraing data:",x_train.shape)
print("Testing data:",x_test.shape)