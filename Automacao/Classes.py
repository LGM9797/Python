'''class LimpadorNome:
    def __init__(self, valor, path):
        if(self.valorValido(valor)):
            self.valor = valor
            self.path = path
        else:
            raise LookupError('Valor inválido')

    def ExtraiArgumentos(self):
        underScore = self.valor.find('2020',2) + len('2020') #Achando o limite da string que quero remover
        newName = self.path +r"/" + self.valor[:underScore]+'.xlsx' #tirando o slice que preciso passar de volta
        return newName


    @staticmethod
    def valorValido(valor):
        if (valor):
            return True
        else:
            return False
        '''

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here

    x = range(1,n+1)
    for i in x:
        if (i % 3 == 0 and i % 5 == 0 and i!=0):
            print('FizzBuzz')
        elif (i % 3 == 0 and i % 5 != 0):
            print('Fizz')
        elif (i % 5 == 0 and i % 3 != 0):
            print('Buzz')
        else:
            print(i)

# n = int(input().strip())
n = 15
fizzBuzz(n)
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     fizzBuzz(n)
