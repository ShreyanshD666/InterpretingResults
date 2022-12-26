import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finalGravityStars.csv")
df.head()

df.drop(['Unnamed: 0'],axis =1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

plt.title("Star Name vs Mass")
plt.xlabel("Star_name")
plt.ylabel("Mass")
plt.show()

plt.title("Star Name vs Radius")
plt.xlabel("Star_name")
plt.ylabel("Radius")
plt.show()

plt.title("Star Name vs Distance")
plt.xlabel("Star_name")
plt.ylabel("Distance")
plt.show()

plt.title("Star Name vs Gravity")
plt.xlabel("Star_name")
plt.ylabel("Gravity")
plt.show()
