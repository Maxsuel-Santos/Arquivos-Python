import pandas as pd

df = pd.read_csv("data.csv")

df.fillna(130, inplace = True) # Substitua os valores NULL pelo número 130:

print(df.to_string())

'''
O exemplo acima substitui todas as células vazias em todo o Data Frame.

Para substituir apenas valores vazios por uma coluna, especificar nome da coluna para o DataFrame:
'''

df["Calories"].fillna(130, inplace = True) # Ao invés de substituir tudo que for nulo, só substituirá onde for nulo em Calories

print(df.to_string())
