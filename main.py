import pandas as pd
import numpy as np
import xlrd
import openpyxl

a = pd.ExcelFile('imiona.xlsx')
da = pd.read_excel(a, header=0)
print(da)
