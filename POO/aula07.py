# Atributo de classe
class Pessoa:
    anoAtual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # Função apenas demonstratica, essa não é a melhor forma de calcular idade
    def get_anoNascimento(self):
        return Pessoa.anoAtual - self.idade
    
p1 = Pessoa('João', 35)
print(p1.get_anoNascimento())

p2 = Pessoa('Helena', 12)
print(p2.get_anoNascimento())
