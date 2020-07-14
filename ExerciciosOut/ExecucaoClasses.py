# -*- coding: utf-8 -*-


from ClassesExec import *
"""
Bola1 = Bola('Azul', 10, 'ABS')
Bola1.MostraCor()
Bola1.TrocaCor('Verde')
Bola1.MostraCor()
"""
"""
quad1 = Quadrado(10)
quad1.MudarValorLado(15)
quad1.MudarValorLado(-10)
print(quad1.get_ValorLado())
print(quad1.Area())
"""
"""

ret1 = Retangulo(10, 50)
ret1.AlterarAltura(25)
ret1.AlterarBase(15)
ret1.get_Valores()
ret1.AreaRetangulo()
ret1.PerimetroRetangulo()

"""

"""
base = input('Insira a medida da base: ')
altura = input('Insira a medida da altura: ')

ret1 = Retangulo(base, altura)
area = ret1.get_AreaRetangulo()
perimetro = ret1.get_PerimetroRetangulo()

print(f'Quantidade de piso: {area} m2 e a quanidade de rodapés {perimetro}m')
"""
"""
lucas = Pessoa('Lucas', 19, 100, 1.80)

print(lucas.Get_Peso())
print(lucas.Get_Altura())
print(lucas.Get_Idade())

print(f'A pessoa se chama {lucas.nome} tem {lucas.Get_Idade()} anos e mede {lucas.Get_Altura()} metros')
"""

"""
tv1 = TV(5, 0)
print(tv1.Canal)
tv1.EscolherCanal(14)
print(tv1.Canal)
print(tv1.Volume)
tv1.AbaixarVolume()
print(tv1.Volume)
"""

carro1 = Carro(10)
print(f'Esse eh o consumo inicial do carro {carro1.Consumo}')
carro1.Abastecer(10)
print(f'Esse eh o nivel do tanque apos abastecer {carro1.NivelTanque}')
carro1.Andar(10)
print(f'Nivel do tanque depois de andar 10km {carro1.NivelTanque} litros ')
