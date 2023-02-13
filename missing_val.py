import pandas as pd

Dataset = pd.read_csv('stores.csv')
columns = Dataset.columns

missing_list = [(Dataset.isnull()).sum()]

for i in missing_list:
    print(str(i).split(" "))

