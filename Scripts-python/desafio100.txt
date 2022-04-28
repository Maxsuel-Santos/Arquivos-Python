print('\033[1;31m-=-\033[m' * 15)
print('=== PROGRESSÃO ARITMÉTICA ===')
print('\033[1;31m-=-\033[m' * 15)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='- ')
print('ACABOU!')
