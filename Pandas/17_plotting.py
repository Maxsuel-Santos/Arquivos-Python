'''
Pandas usa o plot() método para criar diagramas.

Podemos usar o Pyplot, um submódulo da biblioteca Matplotlib para visualizar o diagrama na tela.

Instale o Matplotlib: Vá no cmd do terminal e digite: pip install matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

'''
Gráfico de dispersão
Especifique que você deseja um gráfico de dispersão com o kind argumento:

kind = 'scatter'

Um gráfico de dispersão precisa de um eixo x e y.

No exemplo abaixo, usaremos "Duração" para o eixo x e "Calorias" para o eixo y.

Inclua os argumentos xey como este:

x = 'Duration', y = 'Calories'
'''

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

# Uma trama de dispersão em que não há relação entre as colunas:

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

'''
Histograma
Use o kind argumento para especificar que você deseja um histograma:

kind = 'hist'

Um histograma precisa de apenas uma coluna.

Um histograma mostra a frequência de cada intervalo, por exemplo quantos exercícios duraram entre 50 e 60 minutos?

No exemplo abaixo, usaremos a coluna "Duração" para criar o histograma:
'''

df["Duration"].plot(kind = 'hist')
plt.show()
