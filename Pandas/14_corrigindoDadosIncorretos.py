'''
"Dados incorretos" não precisa ser "células vazias" ou "formato incorreto", pode apenas esteja errado, como se alguém tivesse registrado "199" em vez de "1,99".

Às vezes, você pode detectar dados errados olhando para o conjunto de dados, porque você espera o que deveria ser.

Se você der uma olhada no nosso conjunto de dados, poderá ver que na linha 7, a duração é 450, mas para todas as outras linhas a duração é entre 30 e 60.

Não precisa estar errado, mas levando em consideração que este é o conjunto de dados do treino de alguém sessões, concluímos com o fato de que essa pessoa não deu certo em 450 minutos.
'''

import pandas as pd

df = pd.read_csv("data2.csv")

# Substituindo valores
df.loc[7, 'Duration'] = 45 # Para conjuntos de dados pequenos, você poderá substituir os dados errados um por um, mas não para conjuntos de big data.

# Para substituir dados errados por conjuntos de dados maiores, você pode criar algumas regras, por exemplo. defina alguns limites para valores legais e substitua quaisquer valores que estejam fora do limites.

#Faça um loop em todos os valores na coluna "Duração. Se o valor for maior que 120, defina-o como 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Remoção de linhas
#Outra maneira de lidar com dados incorretos é remover as linhas que contêm dados errados. Dessa forma, você não precisa descobrir com o que substituí-los e existe uma boa chance de você não precisar deles para fazer suas análises.

# Exclua linhas em que "Duração" é maior que 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

