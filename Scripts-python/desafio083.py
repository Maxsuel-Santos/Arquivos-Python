print('=== AUMENTOS MÚLTIPLOS ===')
salário = float(input('Qual o salário do funcionário? '))
print('--------------------------------------------')
if salário <= 1250:
    print('Seu novo salário com 15% de aumento será: R$ {:.2f}'.format(salário + (salário * 15 / 100)))
else:
    print('Seu novo salário com 10% de aumento será: R$ {:.2f}'.format(salário + (salário * 10 /100)))
print('-=-=-=-=-=-=FIM-=-=-=-=-=-=')
