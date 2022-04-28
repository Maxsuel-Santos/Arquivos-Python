import math
print('=== SENO, COSSENO & TANGENTE ===')
print('-------------------------------------------------------------------')
ang = float(input('Informe o ângulo: '))
print('-------------------------------------------------------------------')
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Ângulo: {} \nSeno: {:.3f} \nCosseno: {:.3f} \nTangente: {:.3f}'.format(ang, seno, cosseno, tangente))
print('-------------------------------------------------------------------')


print('-------------------------------------------------------------------')
# OUTRA MANEIRA DE RESOLUÇÃO
print('-------------------------------------------------------------------')


from math import radians, sin, cos, tan
print('=== SENO, COSSENO & TANGENTE ===')
ang = float(input('Informe o ângulo: '))
print('-------------------------------------------------------------------')
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('Ângulo: {} \nSENO: {:.3f} \nCOSSENO: {:.3f} \nTANGENTE: {:.3f}'.format(ang, seno, cosseno, tangente))

