print('=== SORTEANDO UMA ORDEM NA LISTA ===')
print('--------------------------------------')
import random
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))
print('--------------------------------------')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem será: {lista}')


print('-------------------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
print('-------------------------------------------------------------------')


print('=== SORTEANDO UMA ORDEM NA LISTA ===')
print('--------------------------------------')
from random import shuffle
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))
print('--------------------------------------')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem será: {lista}')
