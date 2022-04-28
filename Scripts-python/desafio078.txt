print('=== RADAR ELETRÔNICO === 🚗🚓🚕🛺🚙🚌🚐🚎🚑🚒🚚🚛🚜🚘🚔🚖🚍🦽🚲🛹🛴🛵🏍🏎')
print('-=-' * 50)
km = float(input('Quantos km/h o veículo está? '))
print('-=-' * 20)
if km > 80:
    multa = (km - 80) * 7
    print('Você está à cima do limite de velocidade permitido de 80 km/h. \nVocê irá pagar R$ {:.2f} de multa.'.format(multa))
    print('-=-' * 100)
else:
    print('Você está no limete de velocidade. Continue assim!')
print('Dirija com cuidado. Tenha um bom dia!')
print('-=-' * 20)
print('                                               -=-=-=-=-=-=FIM-=-=-=-=-=-=-')
print('_-_-' * 50)