import pandas as pd
data={ "Name":["Rahul","Subrata","Rita","Biltu","Jit","Akash"],"Marks":[95,84,90,63,99,78]}
df= pd.DataFrame(data)
print(df)
print("Studentd name")
print(df["Name"])
print("Studentd marks")
print(df["Marks"])
print("/n Highest marks")
print(df["Marks"].max())
print("/n Average marks")
print(df["Marks"].mean())
print("/n [Marks]>80")
print(df[df["Marks"]>80])
