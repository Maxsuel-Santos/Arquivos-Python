print('\033[1;31m-=-\033[m' * 15)
print('=== MAIOR E MENOR VALORES ===')
print('\033[1;31m-=-\033[m' * 15)
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média entre eles foi de {media} '
      f'\nO maior número foi {maior} e o menor número foi {menor}')
print('FIM')
