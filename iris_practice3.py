from sklearn.datasets import load_iris
iris= load_iris()
print(iris.keys())
print("/n Features")
print(iris.feature_names)
print("/n Flower names")
print(iris.target_names)
print("/n first 5 flower names")
print(iris.data[:5])