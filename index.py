from time import sleep

def linha():
    print('\033[1;33m-\033[m'*40)

    
cont = 0
op = ''
while True:
    linha()
    id = int(input((f'Digite a idade: ')))
    if id > 18:
        cont += 1
    op = str(input('Deseja continuar? (s/n): ')).lower()[0]
    linha()
    if op == 'n':
        break
    else:
        continue
print('ANALIZANDO...') 
sleep(3)
linha()
print(f'Ao total, foram {cont} pessoa(s) maiores de idade.')
linha()
