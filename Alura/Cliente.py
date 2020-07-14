# -*- coding: utf-8 -*-
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()  # title faz a primeira letra ser maiuscula

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


cliente1 = Cliente('lucas')


print(cliente1.nome)
cliente1.nome = 'nico'
print(cliente1.nome)
