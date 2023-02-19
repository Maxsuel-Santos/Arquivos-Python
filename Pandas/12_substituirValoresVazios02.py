import pandas as pd

df = pd.read_csv("data.csv")

# Calcule a MÉDIA (mpedia entre todas as calorias) e substitua quaisquer valores vazios por ele:
x = df["Calories"].mean() 
df["Calories"].fillna(x, inplace = True) # Média = o valor médio ( a soma de todos os valores divididos pelo número de valores ).

# Calcule a MEDIANA e substitua quaisquer valores vazios por ele:
x = df["Calories"].median() 
df["Calories"].fillna(x, inplace = True) # Mediana = o valor no meio, depois de classificar todos os valores ascendente.

# Calcule o MODO e substitua quaisquer valores vazios por ele:
x = df["Calories"].mode()[0] # Armazena na variável x
df["Calories"].fillna(x, inplace = True) # Modo = o valor que aparece com mais frequência.
