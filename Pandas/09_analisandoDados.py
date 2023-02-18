import pandas as pd

data = pd.read_csv("data.csv")

''' 
O método head() retorna os cabeçalhos e um número especificado de linhas, começando do topo.
Observação: se o número de linhas não for especificado, o método head() retornará as 5 primeiras linhas.
'''
print(f"{data.head(10)}")

'''
O método tail() retorna os cabeçalhos e um número especificado de linhas, começando da parte inferior.
Observação: se o número de linhas não for especificado, o método tail() retornará as 5 últimas linhas.
'''
print(f"{data.tail(7)}")

print(f"{data.info()}") # Fornece mais informações sobre o conjunto de dados.

'''
O método info() também nos informa quantos valores não nulos estão presentes em cada coluna e, em nosso conjunto de dados, parece que há 164 de 169 valores não nulos na coluna "Calorias".

O que significa que existem 5 linhas sem valor algum, na coluna "Calorias", por qualquer motivo.

Valores vazios, ou valores nulos, podem ser ruins ao analisar dados e você deve considerar a remoção de linhas com valores vazios. Este é um passo em direção ao que é chamado de limpeza de dados , e você aprenderá mais sobre isso nos próximos capítulos.
'''
