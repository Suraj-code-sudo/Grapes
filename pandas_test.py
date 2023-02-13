import pandas as pd

df = pd.read_csv('E:/EY_projects/CSV_UPLOAD/optimized_csv/person_100.csv')
columns = df.columns
row_count = [df[column].count() for column in df.columns]
missing_values = list((df.isnull()).sum())
types = (df.dtypes)

json_list = []
for i in range(len(columns)):
    json_list.append(dict([("columns", columns[i]), ("row_count", row_count[i]), ("miss_value", missing_values[i])]))
print(json_list)
json_val = {"values":json_list}
print(json_val)
