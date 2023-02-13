import pandas as pd

data = {
    'name':['suraj', 'harish'],
    'course':['cse', 'ece']
}
dataframes = pd.DataFrame(data)
print(dataframes[['name']])