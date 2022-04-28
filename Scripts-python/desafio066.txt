print('=== Catetos ===')
print('-------------------------------------------------------')
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
print('-------------------------------------------------------')
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
print('-------------------------------------------------------')


print('-------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO LOGO ABAIXO
print('-------------------------------------------------------')


print('=== Catetos e Hipotenusa - Atualizado ===')
from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
print('-------------------------------------------------------')
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))
