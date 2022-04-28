print('\033[1;31m-=-\033[m' * 15)
print('=== GRUPO DE MAIORIDADE ===')
print('\033[1;31m-=-\033[m' * 15)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoa(s) maior(es) de idade.'.format(totmaior))
print('Também tivemos {} pessoa(s) menor(es) de idade'.format(totmenor))
