
# -*- coding: utf-8 -*-

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def TrocaCor(self, NovaCor):
        self.__cor = NovaCor

    def MostraCor(self):
        print(self.__cor)


class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def MudarValorLado(self, NovoValor):
        if(NovoValor > 0):
            self.__lado = NovoValor
        elif(NovoValor < 0):
            print("Valor Inválido")

    def get_ValorLado(self):
        return self.__lado

    def Area(self):
        print(self.__lado * self.__lado)


class Retangulo:
    def __init__(self, base, altura):
        self.__base = int(base)  # metodo 'privado'
        self.__altura = int(altura)  # metodo 'privado'

    def AlterarBase(self, NovoValor):
        self.__base = NovoValor

    def AlterarAltura(self, NovoValor):
        self.__altura = NovoValor

    def get_Valores(self):
        return print(f'O valor da altura é {self.__altura} e da base {self.__base}')

    def get_AreaRetangulo(self):
        Area = self.__base * self.__altura
        return Area
        # print(f'A área do Retangulo é: {Area}')

    def get_PerimetroRetangulo(self):
        Perimetro = 2 * (self.__base + self.__altura)
        return Perimetro
        # print(f'O Perimetro do Retangulo é: {Perimetro}')


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def Envelhecer(self):
        self.__idade += 1

    def Engordar(self, quilos):
        self.__peso += quilos

    def Emagrecer(self, quilos):
        self.__peso -= quilos

    def Crescer(self):
        if(self.__idade < 21):
            self.__altura += 0.05
        else:
            print('Vc n cresce mais abestado')

    def Get_Idade(self):
        return self.__idade

    def Get_Peso(self):
        return self.__peso

    def Get_Altura(self):
        return self.__altura


class TV:

     def __init__(self, canal, volume):
        self.__canal = canal
        self.__volume = volume

     def __CanalValido(self, canal):
        canais = 12
        return canal <= canais

     def __VolumeValido(self, volume):
        if(self.__volume < 100 and self.__volume > 0):
            return True

     def EscolherCanal(self, canal):
        if(self.__CanalValido(canal)):
            self.__canal = canal
        else:
            print('Canal não disponivel')

     def AumentarVolume(self):
        self.__volume += 1
        if(self.__VolumeValido(self.__volume) != True):
            print('Volume inválido')
            self.__volume -= 1

     def AbaixarVolume(self):
        self.__volume -= 1
        if(self.__VolumeValido(self.__volume) != True):
            print('Volume inválido')
            self.__volume += 1

     @property
     def Canal(self):
         return self.__canal

     @property
     def Volume(self):
         return self.__volume


class Carro:
    def __init__(self, consumo):
        self.__consumo = consumo
        self.__nivelCombustivel = 0

    def Andar(self, km):
        CombustivelGasto = km//self.__consumo
        self.__nivelCombustivel -= CombustivelGasto

    def Abastecer(self, litros):
        self.__nivelCombustivel += litros

    @property
    def NivelTanque(self):
        return self.__nivelCombustivel

    @property
    def Consumo(self):
        return self.__consumo

#
# class Posto:
#     def __init__(self,tanques,endereco):
#         self.tanques = tanques
#         self.endereco = endereco

class BombaCombustivel:
    def __init__(self, tipoComb, valorLitro, qtdComb):
        self.tipoComb = tipoComb
        self.valorLitro = valorLitro
        self.qtdComb = qtdComb


    def abastecerValor(self, valor):
        pass

    def abastecerLitros(self, litros):
        pass

    def alterarValor(self,valor):
        self.valorLitro = valor
        pass

    def alterarComb(self, tipo):
        self.tipoComb = tipo
        pass

    def alterarQtdComb(self, valor):
        self.qtdComb -= valor





