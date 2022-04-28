print('=== SEPARANDO DÍGITOS DE NÚMERO ===')
print('--------------------------------------------------------')
num = int(input('Digite um número inteiro entre 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('--------------------------------------------------------')
print('--------------------------------------------------------')
print(f'Analizando o número {num}.')
print('--------------------------------------------------------')
print('--------------------------------------------------------')
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
print('--------------------------------------------------------')