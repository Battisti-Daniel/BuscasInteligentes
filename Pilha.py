class Pilha:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1
        
    def empilhar(self, cidade):
        if not self.pilhaCheia():
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print('Opss... Parece que a pilha já esta cheia')
        
    def desempilhar(self):
        if not self.pilhaVazia():
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp.nome
        else:
            print('Opss... Parece que a pilha já esta vazia')
            return None
    
    def getTopo(self):
        return self.cidades[self.topo]
    
    def pilhaVazia(self):
        return self.topo == -1
    
    def pilhaCheia(self):
        return self.topo == self.tamanho - 1
    
    
from Mapa import Mapa

mapa = Mapa()

pilha = Pilha(5)

pilha.empilhar(mapa.portoUniao)
pilha.empilhar(mapa.campoLargo)
pilha.empilhar(mapa.canoinhas)

pilha.desempilhar()