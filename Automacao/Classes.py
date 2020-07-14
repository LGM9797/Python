class LimpadorNome:
    def __init__(self, valor, path):
        if(self.valorValido(valor)):
            self.valor = valor
            self.path = path
        else:
            raise LookupError('Valor inválido')

    def ExtraiArgumentos(self):
        underScore = self.valor.find('2020') + len('2020') #Achando o limite da string que quero remover
        newName = self.path + '/' + self.valor[:underScore] #tirando o slice que preciso passar de volta
        return newName

    @staticmethod
    def valorValido(valor):
        if (valor):
            return True
        else:
            return False