print('=== ANO BISSEXTO ===')
from time import sleep
from datetime import date
ano = int(input('Que ano você quer analizar? Digite 0 para analizar o ano atual. '))
print('ANALIZANDO...')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO.'.format(ano))
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')
print('-=-=-=-=-=-=FIM-=-=-=-=-=-=')
