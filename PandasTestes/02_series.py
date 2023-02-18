import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a) # Índices automáticos (a partir do 0)
myvar2 = pd.Series(a, index = ["X", 
                               "Y", 
                               "Z"]) # Índices manuais (você define)
calories = {"day1": 420, 
            "day2": 380, 
            "day3": 390} # Objeto como índice {dicionário}

print(myvar)
print(myvar[0])

print("==================================")

print(myvar2)
print(myvar2["X"]) # Consultando pelo índice passado

print("==================================")
myvar3 = pd.Series(calories)
print(myvar3)
print(pd.Series(calories, index = ["day1", "day2"])) # Exibindo por filtro (day1 e day2)
