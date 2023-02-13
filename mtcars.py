import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/Suraj/Downloads/mtcars.csv")
x = (df['mpg'])
y = df['wt']
plt.scatter(x, y)
plt.show()