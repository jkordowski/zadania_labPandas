import pandas as pd
import numpy as np

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')

## lista unikalnych nazwisk sprzedawców
# df1 = df.Sprzedawca
# df1 = df1.drop_duplicates()
# print(df1)

## 5 najwyższych wartości zamówień
# df2 = df
# df2.Utarg = df2.Utarg.astype(float)
# df2 = df2.sort_values(by='Utarg', ascending=False)
# print(df2['Utarg'].head(5))

## ilośc zamówień każdego sprzedawcy
# print(df.groupby(['Sprzedawca']).agg({'Sprzedawca': ['count']}))

##suma zamówień każdego kraju
# print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))

##suma zamówień w 2005 dla sprzedawców z Polski
# df5 = df[(df['Kraj'] == "Polska")]
start = '2005-01-01'
end = '2005-12-31'
# df5 = df5[(df5['Data zamowienia'] >= start) & (df5['Data zamowienia'] <= end)]
# print(df5)

##średnia kwota w 2004
start2 = '2004-01-01'
end2 = '2004-12-31'
# df6 = df[(df['Data zamowienia'] >= start2) & (df['Data zamowienia'] <= end2)]
# df6 = df6.Utarg
# df6 = pd.to_numeric(df6, downcast='float')
# print(df6.mean())

##zapisz dane za 2004 do pliku 2004 i 2005 do pliku 2005
# df2004 = df[(df['Data zamowienia'] >= start2) & (df['Data zamowienia'] <= end2)]
# df2005 = df[(df['Data zamowienia'] >= start) & (df['Data zamowienia'] <= end)]
# df2004.to_csv('zamówienia_2004.csv', sep=';', header=True, index=False)
# df2005.to_csv('zamówienia_2005.csv', sep=';', header=True, index=False)