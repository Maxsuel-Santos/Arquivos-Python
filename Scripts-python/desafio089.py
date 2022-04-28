print('=== AQUELE CLÁSSICO DA MÉDIA ===')
print('\033[1;33m-=-\033[m' * 25)
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
med = (n1 + n2 + n3 + n4) / 4
print('\033[1;33m-=-\033[m' * 25)
if med < 5:
    print('Sua média foi {:.2f}. \nVocê foi \033[1;31mREPROVADO\033[m.'.format(med))
elif med > 5 and med < 7:
    print('Sua média foi {:.2f}. \nVocê está em \033[1;33mRECUPERAÇÃO\033[m.'.format(med))
else:
    print('Sua média foi {:.2f}. \nVocê foi \033[32mAPROVADO\033[m.'.format(med))
print('\033[1;30m-=-=-=-=-=FIM-=-=-=-=-=\033[m')
