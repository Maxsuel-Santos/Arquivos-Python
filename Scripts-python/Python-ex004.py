print('\033[1;31m-=-\033[m' * 15)
print('=== TRATANDO VÁRIOS VALORES V.1.0 ===')
print('\033[1;31m-=-\033[m' * 15)
cont = soma = num =0
num = int(input('Digite um valor [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um valor [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')


print('\033[1;31m-=-\033[m' * 15)
# OUTRA FORMA DE RESOLUÇÃO (Mais leiga)
print('\033[1;31m-=-\033[m' * 15)

cont = soma = num =0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    cont += 1
    soma += num
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}')