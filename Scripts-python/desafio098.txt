print('\033[1;31m-=-\033[m' * 15)
print('=== TABUADA V.2.0 ===')
print('\033[1;31m-=-\033[m' * 15)
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
