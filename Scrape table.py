import pandas as pd
import numpy as np

inputurl = "https://es.wikipedia.org/wiki/Chile"

dflist = pd.read_html(inputurl, attrs={"class": ["wikitable"]},  header=1)

df = dflist[0]
df.columns.values[0] = "Región"
df.columns.values[1] = "Población"
df.columns.values[2] = "Superficie"
df.columns.values[3] = "Densidad"
df.columns.values[4] = "Capital"

df.drop('Mapa administrativo', axis=1, inplace=True)

df.drop(df.tail(1).index,inplace=True)

array = np.array(df["Población"])

total=0
for num in array:
    numStr=num.replace(u'\xa0', "")
    numStr=numStr.replace(' ', "")
    total = int(numStr) + total
print(total)

def multiplicar(x):
    x=x.replace(u'\xa0', "")
    x=x.replace(' ', "")
    percent=format(float(x)*100/float(total), '.2f')
    return "%"+percent

df["Porcentaje población"] = df["Población"].apply(multiplicar)

df.to_csv('resultado.csv', encoding='utf-8-sig')