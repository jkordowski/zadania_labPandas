import pandas as pd
import numpy as np
import xlrd
import openpyxl

a = pd.ExcelFile('imiona.xlsx')
da = pd.read_excel(a, header=0)

## liczba nadanych imion < 1000
# print(da[da['Liczba'] < 1000])

## nadane imie jest takie jak twoje
# print(da[da['Imie'] == 'JAKUB'])

## suma wszystkich dzieci
# print(da['Liczba'].sum())

## suma dzieci z 2005-2010
# da4 = (da[(da.Rok >= 2005) & (da.Rok <= 2010)])
# print(da4['Liczba'].sum())

## suma chłopców z 2000
# da5 = (da[(da.Rok == 2000) & (da.Plec == 'M')])
# print(da5['Liczba'].sum())

# male = da[da.Plec == 'M']
# female = da[da.Plec == 'K']

## najbardziej popularne imiona w danym roku
# x = male.loc[male.groupby('Rok')['Liczba'].idxmax()]
# y = female.loc[female.groupby('Rok')['Liczba'].idxmax()]
# print(x[['Rok', 'Imie']])
# print(y[['Rok', 'Imie']])

## najbardziej poppularne imie M i K w calym okresie
# maxMale = male.loc[male['Liczba'].idxmax()]
# maxFemale = female.loc[female['Liczba'].idxmax()]
# print(maxMale.Imie, maxFemale.Imie)


# print(da.groupby(['Rok', 'Plec'])['Liczba'].max())
# (da.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']}))



