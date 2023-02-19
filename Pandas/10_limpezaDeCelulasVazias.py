'''
Limpeza de dados significa corrigir dados incorretos no seu conjunto de dados.

Dados incorretos podem ser:

Células vazias
Dados em formato errado
Dados incorretos
Duplicatas
'''

import pandas as pd

df = pd.read_csv("data.csv")

new_df = df.dropna() # Retorna um Data Frame sem as células vazias e não alterará o original (remove a célula que tenha algum dado null).

df.dropna(inplace = True) # Se você deseja alterar o DataFrame original, use o inplace = True
# Nota: Agora, o dropna(inplace = True) NÃO retornará um novo DataFrame, mas removerá todas as linhas que contêm valores NULL do DataFrame original.

#print(new_df.to_string())
print(df.to_string())
