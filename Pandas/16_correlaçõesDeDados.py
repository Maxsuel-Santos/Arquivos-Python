import pandas as pd

df = pd.read_csv("data.csv")

print(df.corr()) # Mostre o relacionamento entre as colunas
# Nota: O método corr() ignora "não numérico" colunas.

'''
Resultado explicado
O resultado do corr() método é uma tabela com muitos números que representa quão bem o relacionamento é entre duas colunas.

O número varia de -1 a 1.

1 significa que existe uma relação de 1 a 1 ( uma correlação perfeita ), e para esse conjunto de dados, cada vez que um valor era aumentado na primeira coluna, o outro também subia.

0,9 também é um bom relacionamento e, se você aumentar um valor, o outro provavelmente também aumentará.

-0,9 seria um relacionamento tão bom quanto 0,9, mas se você aumentar um valor, o outro provavelmente cairá.

0.2 significa NÃO um bom relacionamento, o que significa que se um valor subir, não significa que o outro o fará.

O que é uma boa correlação? Depende do uso, mas acho seguro dizer que você precisa ter pelo menos 0.6 ( ou -0.6) para chamá-lo de uma boa correlação.
'''

