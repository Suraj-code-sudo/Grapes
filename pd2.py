import openpyxl
import pandas as pd
import openpyxl
dataset = openpyxl.load_workbook("sampledatafoodsales.xlsx")
sheet = dataset.active
print(sheet.values)