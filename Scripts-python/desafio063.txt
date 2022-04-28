print('\033[1;31m-=-\033[m' * 15)
print('=== SEQUÊNCIA DE FIBONACCI V.1.0 ===')
print('\033[1;31m-=-\033[m' * 15)
print('---' * 10)
print('Sequência de Fibonacci')
print('---' * 10)
n = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('~~~~' * 10)
print(f'{t1} - {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'- {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('~~~' * 10)
