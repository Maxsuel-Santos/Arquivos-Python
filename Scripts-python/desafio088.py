print('=== ALISTAMENTO MILITAR ===')
print('\033[1;33m-=-\033[m' * 25)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
print('Qual seu sexo: [ 1 ] Masculino. [ 2 ] Feminino.')
sex = int(input('Seu sexo: '))
print('\033[1;33m-=-\033[m' * 25)
idade = atual - nasc
print(f'Você nasceu em {nasc} tem/terá {idade} anos em {atual}.')
if sex == 2:
    print('\033[1;31mVocê não pode se alistar. É apenas para HOMENS.\033[m')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para seu alistamento.')
    ano = atual + saldo
    print(f'Seu alistametno será em {ano} ')
else:  # idade > 18
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} ano(s).')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;30m-=-=-=-=-=FIM-=-=-=-=-=\033[m')
