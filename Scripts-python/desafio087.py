print('=== COMPARANDO NÚMEROS ===')
print('\033[1;33m-=-\033[m' * 25)
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um segundo número inteiro: '))
print('\033[1;33m-=-\033[m' * 25)
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num2 > num1:
    print(f'O número {num2} é maior que o número {num1} ')
else:
    print('Não existe número maior, os dois são iguais. :)')
print('\033[1;33m-=-\033[m' * 25)
print('\033[7;30m-=-=-=-=-=FIM-=-=-=-=-=\033[m')
