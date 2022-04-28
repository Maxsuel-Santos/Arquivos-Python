print('=== TRUNC de números reais ====')
print('-----------------------------------------------------')
from math import trunc
num = float(input('Informe um número real pra ver sua parte inteira: '))
print('-----------------------------------------------------')
result = trunc(num)
print('O número {} tem como parte inteira: {}'.format(num, result))
print('-------------------------------------------------------')


print('-------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
''' OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO '''
print('-------------------------------------------------------')


from math import floor
num = float(input('Digite um número: '))
result = floor(num)
print(f'O número {num} tem como parte inteira: {result}')


print('-------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
''' OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO '''
print('-------------------------------------------------------')


num = float(input('Digite um número: '))
print(f'O número {num} tem como parte inteira: {int(num)}')
