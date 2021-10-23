import pandas as pd

df=pd.read_csv('scraped-final.csv')
print(df.shape)
print(list(df))

del df["id"]
del df["id.1"]
del df["id.2"]
del df["name"]
del df["distance.1"]
del df["mass.1"]
del df["radius.1"]
del df["luminosity"]

print(df.shape)
print(list(df))

df.to_csv("real_final.csv")