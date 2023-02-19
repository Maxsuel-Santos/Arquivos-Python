import pandas as pd

df = pd.read_csv("data2.csv")

df['Date'] = pd.to_datetime(df['Date']) #Como você pode ver no resultado, a data na linha 26 foi fixa, mas a data vazia na linha 22 obteve um valor de NaT ( Não é um valor de Time, é NULL), ou seja, um valor vazio. Uma maneira de lidar com valores vazios é simplesmente remover a linha inteira.

#print(df.to_string())

# Remoção de linhas
# Remova linhas com um valor NULL na coluna "Date":
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())