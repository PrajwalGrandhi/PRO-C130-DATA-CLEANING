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

final_data=df.dropna()
final_data.reset_index(drop=True,inplace=True)
final_data.to_csv("real_final.csv")
