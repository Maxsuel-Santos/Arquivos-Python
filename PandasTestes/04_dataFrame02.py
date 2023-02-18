import pandas as pd

'''
    Um Pandas DataFrame é uma estrutura de dados bidimensional, como uma matriz bidimensional ou uma tabela com linhas e colunas.
'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# Carrega dados em um objeto DataFrame:
df = pd.DataFrame(data)

#print(df) 
print(df.loc[0]) # loc[] -> pega o valor do índice que você deseja (retorna uma série em pandas), neste caso, retorna todos os valores de índice 0 (420 e 50). Só pode usar o loc com aspas se usar o index para dar nome no lugar dos índice

print(df.loc[[0, 1]]) # Retorna as linhas 0 e 1
