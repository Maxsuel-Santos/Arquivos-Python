print('=== MAIOR E MENOR VALORES ===')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
print('--------------------------')
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor foi {}. \nO menor valor foi {}.'.format(maior, menor))
print('-=-=-=-=-=-=FIM-=-=-=-=-=-=')
