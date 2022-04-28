print('\033[1;31m-=-\033[m' * 15)
print('=== SUPER PROGRESSÃO ARITMÉTICA V.3.0 ===')
print('\033[1;31m-=-\033[m' * 15)
print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} - ', end='')
        contador += 1
        termo += razao
    print('PAUSA')
    mais = int(input('(Pressione 0 para terminar) Quantos termos você gostaria de ver a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
