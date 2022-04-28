print('\033[1;31m-=-\033[m' * 15)
print('=== SOMA ÍMPARES MÚLTIPLOSDE TRÊS ===')
print('\033[1;31m-=-\033[m' * 15)
soma = 0
cont = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        cont += 1          # A mesma coisa de cont = cont + 1
        soma += contagem   # A mesma coisa de soma = soma + contagem
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
