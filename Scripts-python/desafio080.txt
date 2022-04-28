print('=== CUSTO DE VIAGEM ===')
print('--' * 13)
km = float(input('Qual a distância da viagem? Km '))
if km <= 200:
    print('Você irá pagar no total R$ {:.2f}'.format(km * 0.50))
else:
    print('Você irá pagar R$ {:.2f}'.format(km * 0.45))
print('--' * 13)
print('-=-=-=-=-=-=Obrigado pela preferência. Volte sempre!-=-=-=-=-=-=')
