print('\033[1;31m-=-\033[m' * 15)
print('=== CONTAGEM REGRESSIVA ===')
print('\033[1;31m-=-\033[m' * 15)
from time import sleep
print('Contagem para os \033[1;32mfogos de artifícil em:\033[m ')
sleep(2.5)
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('\033[1;31m-=-\033[m' * 15)
print('BOOOMMM! 💥╰(*°▽°*)╯')
