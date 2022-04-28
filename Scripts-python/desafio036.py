print('=== APROVANDO EMPRÉSTIMOS ===')
from time import sleep
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos você deseja pagar à casa? '))
print('\033[1;30mANALIZANDO...\033[m')
sleep(3)
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos, a prestação será de R$ {:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('O empréstimo \033[1;32mpode ser concedido.\033[m')
else:
    print('Empréstimo \033[1;31mnegado\033[m!')
print('-=-=-=-=-=FIM-=-=-=-=-=')
