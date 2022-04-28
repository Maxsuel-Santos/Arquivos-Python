print('\033[1;31m-=-\033[m' * 15)
print('=== CÁLCULO DO FATORIAL ===')
print('\033[1;31m-=-\033[m' * 15)
from math import factorial
num = int(input('Digite um número para ver seu fatorial: '))
f = factorial(num)
print(f'O fatorial de {num}! é {f}')


print('\033[1;31m-=-\033[m' * 15)
# OUTRA MANEIRA DE RESOLUÇÃO
print('\033[1;31m-=-\033[m' * 15)


n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
