print('-=-' * 15)
print('=== ANALIZANDO TRIÂNGULO v.1===')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-' * 30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO. ')
print('-=-=-=-=-=-=FIM-=-=-=-=-=-=')