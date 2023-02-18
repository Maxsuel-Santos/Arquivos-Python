import pandas as pd

# OBS: A questão da quatidade máximas de linhas sem usar o to_string() é a mesma com csv
'''
JSON = Dicionário Python
Os objetos JSON têm o mesmo formato dos dicionários Python.
'''

json = pd.read_json("data.json") # Ler arquivo json

print(f"{json.to_string()}")
