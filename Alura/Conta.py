# -*- coding: utf-8 -*-
# Conta
class Conta:

    def __init__(self, numero, titular, saldo, limite):  # Função construtora de objeto
        #print("Construindo objeto ... {}".format(self))
        self.__numero = numero  # atributo privado usar '__'
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do Titular {self.__titular}')

    def deposito(self, valor):
        self.__saldo += valor

    # '__' deixa o metodo privado apenas para a classe q foi criado
    def __saque_autorizado(self, valorSaque):
        valorDispo = self.__saldo + self.__limite
        return valorSaque <= valorDispo

    def saque(self, valor):

        if(self.__saque_autorizado(valor)):
            self.__saldo -= valor
        else:
            print('Não autorizado')

    def transferencia(self, valor, destino):
        self.__saldo -= valor
        destino.deposito(valor)

    @property  # propriedade para acessar o valor do atributo da classe
    def saldo(self):
        return self.__saldo

    @property  # propriedade para acessar o valor do atributo da classe
    def titular(self):
        return self.__titular

    @property  # propriedade para acessar o valor do atributo da classe
    def limite(self):
        return self.__limite

    @limite.setter  # propriedade para alterar o valor do atributo da classe
    def limite(self, valor):
        self.__limite = valor

    # Esse metodo se refere a classe, nao ao objeto (nao eh necessario ter um objeto para acessar esse metodo)
    @staticmethod
    def codBanco():
        return {'BB': '001', 'Caixa': '104'}
