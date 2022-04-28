cont = 0
op = ''
while True:
    id = int(input((f'Digite a idade: ')))
    if id > 18:
        cont += 1
    op = str(input('Deseja continuar? (s/n): ')).lower()[0]
    if op == 'n':
        break
    else:
        continue
print(f'Ao total, foram {cont} pessoas maiores de idade.')


