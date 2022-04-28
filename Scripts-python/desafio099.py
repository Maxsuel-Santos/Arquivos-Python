print('\033[1;31m-=-\033[m' * 15)
print('=== SOMA DOS PARES ===')
print('\033[1;31m-=-\033[m' * 15)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num      # soma += num
        cont = cont + 1        # cont += 1
print('Você informou {} número(s) PARES e a soma foi: {}'.format(cont, soma))
