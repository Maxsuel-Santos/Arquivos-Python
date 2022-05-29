from desafio109 import moeda  # from moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'Aumentando 10% de R$ {moeda.moeda(p)}, temos R$ {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% de R$ {moeda.moeda(p)}, temos R$ {moeda.diminuir(p, 13, True)}')
