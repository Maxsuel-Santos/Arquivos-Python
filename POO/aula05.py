# Escopo da classe e de métodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def alimentar(self, alimento):
        return f'O {self.nome} está comendo {alimento}.'
    
leao = Animal(nome = 'Leão')
print(leao.alimentar('Beterraba'))
