print('\033[1;31m-=-\033[m' * 15)
print('=== DETECTOR DE PALÍNDROMO ===')
print('\033[1;31m-=-\033[m' * 15)
frase = str(input('Digite a frase sem acentuação: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[1;34mTemos um PALÍNDROMO.\033[m')
else:
    print('\033[1;31mA frase digitada não é um palíndromo.\033[m')
