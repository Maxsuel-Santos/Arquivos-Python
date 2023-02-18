import pandas as pd

# (ABAIXO) Permite aumentar o tamanho de linhas a serem exibidas sem usar o to_string()
# pd.options.display.max_rows = 9999 

csv = pd.read_csv("data.csv") # Ler csv (dados separados por vírgulas)

print(f"{csv.to_string()}") # Exibir TODOS os dados do csv (converter para string), para imprimir todos DataFrame use o to_string(), se não só serão exibidas as 50 primeiras e as 5 últimas linhas


