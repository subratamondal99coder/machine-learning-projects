from sklearn.datasets import load_iris
iris= load_iris()
print("Features") 
print(iris.feature_names)
print("/nlower Types:")
print(iris.target_names)
print("/nFirst 5 Flower")
print(iris.data[:5])