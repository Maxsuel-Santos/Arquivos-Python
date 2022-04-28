print('\033[1;31m-=-\033[m' * 15)
print('=== PROGRESSÃO ARITMÉTICA V.2.0 ===')
print('\033[1;31m-=-\033[m' * 15)
print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} - ', end='')
    contador += 1
    termo += razao
print('FIM')
