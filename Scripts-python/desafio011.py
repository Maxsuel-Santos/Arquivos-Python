print('=== Parede e tinta ===')
print('--------------------------------------------------------------')
altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
print('--------------------------------------------------------------')
area = altura * largura
pintura = area / 2
print('Ao total são {} metros de área.'.format(area))
print('São necessários {} litros de tinta para pintar.'.format(pintura))
print('--------------------------------------------------------------')
