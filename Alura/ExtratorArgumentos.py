class ExtratorArgumentos:
    def __init__(self, valor):
        if(self.valorValido(valor)):
            self.valor = valor
        else:
            raise LookupError('Valor inválido')


    @staticmethod
    def valorValido(valor):
        if (valor):
            return True
        else:
            return False

    def ExtraiArgumentos(self):
        underScore = self.valor.find('2020') + 4 #Achando o limite da string que quero remover
        return self.valor[:underScore]

        #print(nome)

