print('=== SORTEANDO DE FORMA ALEATÓRIA ===')
print('-------------------------------------------------------------------')
import random
alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))
print('-------------------------------------------------------------------')
result = random.choice([alu1, alu2, alu3, alu4])
print('O escolhido foi: {}'.format(result))
print('-------------------------------------------------------------------')


print('-------------------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
print('-------------------------------------------------------------------')


print('=== SORTEANDO DE FORMA ALEATÓRIA ===')
print('-------------------------------------------------------------------')
import random
alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))
print('-------------------------------------------------------------------')
lista = [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)
print('O escolhido foi: {}'.format(escolhido))
print('-------------------------------------------------------------------')


print('-------------------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
print('-------------------------------------------------------------------')


print('=== SORTEANDO DE FORMA ALEATÓRIA ===')
print('-------------------------------------------------------------------')
from random import choice
alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))
print('-------------------------------------------------------------------')
lista = [alu1, alu2, alu3, alu4]
escolhido = choice(lista)
print('O escolhido foi: {}'.format(escolhido))
print('-------------------------------------------------------------------')