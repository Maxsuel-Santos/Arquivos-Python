# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando')
            return
        
        print(f'{self.nome} está filmando.')
        self.filmando = True
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} NÃO pode fotografar filmando.')
            return
        
        print(f'{self.nome} está fotografando.')
        
    def paraDeFilmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando')
            return
        
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False
        
c1 = Camera('Canon')
c1.filmar()
c1.fotografar()
c1.paraDeFilmar()

c2 = Camera('Sony')
c2.filmar()
c2.fotografar()
c2.paraDeFilmar()
c2.fotografar()
