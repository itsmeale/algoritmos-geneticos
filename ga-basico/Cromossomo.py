import math, random

class Cromossomo():

    def __init__(self, tamanho):

        self.tamanho = tamanho
        self.valor = ""
        self.avaliacao = -1

    def set_valor(self, novo_valor):

        self.valor = novo_valor
    
    def inicializar(self):

        novo_valor = ""
        for i in range(self.tamanho):
            if random.random() > .5: novo_valor += '1'
            else: novo_valor += '0'
        self.set_valor(novo_valor)

    def crossover(self, outro_cromossomo):

        split_index = int(random.random() * self.tamanho)
        novo_valor = ""
        if random.random() > .5:
            novo_valor = self.valor[0:split_index] + outro_cromossomo.valor[split_index:len(outro_cromossomo.valor)]
        else:
            novo_valor = outro_cromossomo.valor[0:split_index] + self.valor[split_index:len(outro_cromossomo.valor)]
        novo_cromossomo = Cromossomo(self.tamanho)
        novo_cromossomo.set_valor(novo_valor)
        return novo_cromossomo

    def mutacao(self, chance_mutacao):

        inicio, aux, fim = ['','','']
        for i in range(self.tamanho):
            if random.random() < chance_mutacao:
                inicio = self.valor[0:i]
                fim = self.valor[i+1:self.tamanho]
                aux = self.valor[i]
                if aux == '1': aux = '0'
                else: aux = '1'
                self.set_valor(inicio+aux+fim)

    def valor_real(self, inf = 0, sup = 100):

        return inf + (sup - inf)/(2**self.tamanho - 1)*int(self.valor, 2)

    def avaliar(self):

        x = int(self.valor, 2)
        
        self.avaliacao = math.sin(x**2)/(3-math.cos(math.e)-x)
        return self.avaliacao

    def __repr__(self):

        return "cromossomo:[%s] avaliacao[%.2f] valor[%d]" % (self.valor, self.avaliacao, int(self.valor, 2))
        
