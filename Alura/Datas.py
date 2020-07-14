# -*- coding: utf-8 -*-

class DataFormat:

    def __init__(self, dia, mes, ano):
        #print("Construindo objeto ... {}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

        # print(f'{dia}/{mes}/{ano}')

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


data1 = DataFormat(21, 11, 2020)
# print(data1)
data1.formatada()
