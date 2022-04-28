print('=== ANALIZANDO TRIÂNGULOS V2.0 ===')
print('\033[1;33m-=-\033[m' * 25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[1;33m-=-\033[m' * 25)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO ', end='')
    if r1 == r2 == r3:
        print('\033[1;30mEQUILÁTERO.\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;30mESCALENO.\033[m')
    else:
        print('\033[1;30mISÓSCELES.\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')
