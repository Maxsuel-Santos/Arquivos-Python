print('\033[1;31m-=-\033[m' * 15)
print('=== MAIOR E MENOR DA SEQUÊNCIA ===')
print('\033[1;31m-=-\033[m' * 15)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi: {} Kg\nO menor peso lido foi: {} Kg'.format(maior, menor))
