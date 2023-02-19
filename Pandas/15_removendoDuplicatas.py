# Linhas duplicadas são linhas que foram registrados mais de uma vez.
# Para descobrir duplicatas, podemos usar o método duplicated().
# O método duplicated() retorna valores booleanos para cada linha:

import pandas as pd

df = pd.read_csv("data2.csv")

#df.duplicated() # etorna True para cada linha que é uma duplicata, no sentido anti-horário False

# Removendo duplicatas
df.drop_duplicates(inplace = True) # Remova todas as duplicatas

# Lembrar: O (inplace = True) vai verifique se o método NÃO retorna um novo DataFrame, mas ele removerá todos duplicatas do original DataFrame.

print(df.to_string())
