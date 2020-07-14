# -*- coding: utf-8 -*-
"""
1º Faça um Programa que mostre a mensagem "Alo mundo" na tela.
"""


def exec1():
    print('Alô Mundo!')


"""
2º Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""


def exec2():
    n = input("Insira um número: ")
    print("Seu número foi: " + n)


"""
3º Faça um Programa que peça dois números e imprima a soma.
"""


def exec3():
    x = int(input("Insira o 1º número: "))
    y = int(input("Insria o 2º número: "))
    soma = x + y
    print('Seu número foi: {soma}'.format(soma))


"""
4º Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def exec4():
    n1 = int(input("Insira sua n1: "))
    n2 = int(input("Insira sua n2: "))
    n3 = int(input("Insira sua n3: "))
    n4 = int(input("Insira sua n4: "))

    media = (n1 + n2 + n3 + n4) / 4
    print('Sua média foi: {media}'.format(media))


"""
5º Faça um Programa que converta metros para centímetros.
"""


def exec5(metros):
    return metros * 100
# print(exec5(1))


"""
6º Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""


def exec6(r):
    area = (r * r) * 3.14
    return area
# print(exec6(3))


""""
7º Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""


def exec7(l):
    area = l * l
    return area * 2
# print(exec7(100))


"""
8º Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""


def exec8(ValorHora, HorasTrabalhadas):
    return ValorHora * HorasTrabalhadas
#print(f'seu salário foi: {exec8(10,30)}')


"""
9º Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
"""


def exec9(TemperaturaF):
    TempCelsius = 5 * (TemperaturaF - 32) / 9
    return TempCelsius
#print(f'A temperatura em Celsius é : {exec9(90)}')


"""
10º Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""


def exec10(TemperaturaC):
    TempF = TemperaturaC * (9 / 5) + 32
    return TempF
#print(f'A temperatura em Fahrenheit é: {exec10(20)}')


"""
11º Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""


def exec11(n1, n2, n3):
    r1 = (n1 * 2) * (n2 / 2)
    r2 = (n1 * 3) + n3
    r3 = n3 * n3 * n3
    return r1, r2, r3
# print(exec11(10,10,10))


"""
12º Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""


def exec12(Altura):
    return (72.7 * Altura) - 58
# print(exec12(1.80))


"""
13º Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


def exec13(sexo, altura):
    if (sexo.upper() == 'Masculino'.upper()):
        return (72.7 * altura) - 58
    elif (sexo.upper() == 'Feminino'.upper()):
        return (62.1 * altura) - 44.7
# print(exec13('feminino',1.50))


"""
14º João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
 Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
 (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
  João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
   Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
   Imprima os dados do programa com as mensagens adequadas.
"""


def exec14(KgPeixe):
    limite = 50
    excesso = KgPeixe - limite
    multa = excesso * 4.0
    return {'excesso': excesso, 'multa': multa}


"""
peso = int(input("Insira o peso dos peixes:"))
resultado = exec14(peso)
print(f'Excesso = {resultado["excesso"]} KG Multa = R$ {resultado["multa"]}')
#Alternativa: print('Excesso = {e}KG , Multa = R${m}'.format(e=resultado['excesso'], m=resultado['multa']))
"""


"""
15ºFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo
"""


def exec15(salHora, trabHora):
    salario = salHora * trabHora
    ir = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05
    return {'salario_liquido': salario - (inss + ir + sindicato), 'INSS': inss, 'IR': ir, 'sindicato': sindicato, 'salario Bruto': salario}


"""SalarioHora = int(input("Quanto você ganha por hora? :"))
HorasTrabalhadas = int(input("Quantas horas você trabalha? :"))

calculado = exec15(SalarioHora,HorasTrabalhadas)
print(f'Salário Bruto: R${calculado["salario Bruto"]} '
  f'\nIR: R${calculado["IR"]}'
  f'\nINSS: R${calculado["INSS"]}'
  f'\nSindicato {calculado["sindicato"]}'
  f'\nSalário Líquido: R${calculado["salario_liquido"]}')
"""


"""
16º Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


def exec16(MetrosQuadrados):
    litros = MetrosQuadrados / 3
    latas = litros / 18
    preco = latas * 80.00
    return {"latas": latas, "preco": preco}


"""metros = int(input("Insira a M²: "))
calculado = exec16(round(metros))

print(f'A quantidade de latas é de: {calculado["latas"]} e o preço é: R${calculado["preco"]}')
"""


""""
17º Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para
cima, isto é, considere latas cheias.
"""

def exec17(MetrosQuadrados):

    MetrosQuadrados = MetrosQuadrados * 0.10 + MetrosQuadrados

    precoG = 80
    precoP = 25
    litros = MetrosQuadrados / 6
    latasG = litros / 18
    latasG = round(latasG)
    latasP = litros / 3.6
    latasP = round(latasP)
    if(latasG >= 1):
        precoG = latasG * 80
    precoP = latasP * 25

    return {"PrecoG": precoG, "PrecoP": precoP, "LatasG": latasG, "LatasP": latasP}


"""metragem = float(input("Insira a metragem: "))

funcao = exec17(round(metragem))

if(funcao["PrecoG"] < funcao["PrecoP"]):
    print(f'Você precisará de {funcao["LatasG"]} lata(s) de 18L')

elif(funcao['PrecoG']==funcao['PrecoP']):
    print(f'Você precisará de {funcao["LatasG"]} lata(s) de 18L'
          f'\nOu precisará de {funcao["LatasP"]} lata(s) de 3,6L ')

"""


""""
18ºFaça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


def exec18(tamanho, velocidade):
    tempo = ((tamanho * 8) / velocidade) / 60
    return tempo
#print(exec18(100, 1))


"""
Estrutura de Decisão
"""

"""
19º Faça um Programa que peça dois números e imprima o maior deles.
"""


def exec19(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2
# print(exec19(100.1,100))


"""
20º Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""


def exec20(n1):
    if(n1 < 0):
        return 'Número negativo'
    else:
        return 'Número positivo'
# print(exec20(0))


"""
21º Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""


def exec21(letra):
    letra = letra[0].upper()

    if(letra == 'M'):
        return 'Masculino'
    elif(letra == 'F'):
        return 'Feminino'
    else:
        return 'Sexo inválido'
# print(exec21('Masculino'))


"""
22º Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def exec22(letra):
    letra = letra.upper()

    if(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
        return 'Sua letra é uma vogal'
    else:
        return 'Sua letra é uma consoante'
# print(exec22("E"))


"""
23º Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def exec23(n1, n2):
    media = (n1 + n2) / 2

    if(media == 10):
        return 'Aprovado com distinção'
    elif(media >= 7 and media < 10):
        return 'Aprovado'
    elif(media < 7):
        return 'Reprovado'


#print(exec23(9, 9))


"""
24º Faça um Programa que leia três números e mostre o maior deles.
"""


def exec24(n1, n2, n3):
    if(n1 > n2 and n1 > n3):
        return n1
    elif(n2 > n1 and n2 > n3):
        return n2
    elif(n3 > n1 and n3 > n2):
        return n3


#print(exec24(19000, 222, 3333))

"""
25º Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""


def exec25(p1, p2, p3):
    erro = 0

    if (p1 < p2 and p1 < p2):
        valor = p1
    elif(p2 < p1 and p2 < p3):
        valor = p2
    elif(p3 < p1 and p3 < p2):
        valor = p3
    else:
        erro = 1

    if(erro != 1):
        valor = str(valor)
        return 'O produto de valor: R$' + valor + ' é o mais barato'
    else:
        return 'Os produtos possuem o mesmo valor'


"""
prod1 = input('Insira o valor do produto 1: ')
prod2 = input('Insira o valor do produto 2: ')
prod3 = input('Insira o valor do produto 3: ')
print(exec25(prod1, prod2, prod3))
"""

"""
26 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

def exec26(n1, n2, n3):

    Lista = [n1, n2, n3]
    ListaOrdenada = sorted(Lista)
    return ListaOrdenada


#print(exec26(50, 90, 15))

"""
27 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
conforme o caso
"""


def exec27(timeInput):
    timeInput = timeInput.upper()

    if(timeInput == 'M'):
        return 'Bom dia'
    elif(timeInput == 'V'):
        return 'Boa tarde'
    elif(timeInput == 'N'):
        return 'Boa noite'
    else:
        return 'Valor inválido'


# print(exec27('n'))


"""
28 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


def exec28(SalarioAtual):

    if(SalarioAtual <= 280):
        Percentual = 0.20
        Aumento = SalarioAtual * Percentual
        SalarioAjustado = SalarioAtual + Aumento
        return print(f'O seu antigo salário era: R$ {SalarioAtual}'
                     f'\n O seu reajuste foi de: {Percentual*100}%'
                     f'\n O seu aumento foi de R${Aumento}'
                     f'\n O seu novo salário é: R$ {SalarioAjustado}')

    elif(SalarioAtual > 280 and SalarioAtual <= 700):
        Percentual = 0.15
        Aumento = SalarioAtual * Percentual
        SalarioAjustado = SalarioAtual + Aumento
        return print(f'O seu antigo salário era: R$ {SalarioAtual}'
                     f'\n O seu reajuste foi de: {Percentual*100}%'
                     f'\n O seu aumento foi de R${Aumento}'
                     f'\n O seu novo salário é: R$ {SalarioAjustado}')

    elif(SalarioAtual > 700 and SalarioAtual <= 1500):
        Percentual = 0.10
        Aumento = SalarioAtual * Percentual
        SalarioAjustado = SalarioAtual + Aumento
        return print(f'O seu antigo salário era: R$ {SalarioAtual}'
                     f'\n O seu reajuste foi de: {Percentual*100}%'
                     f'\n O seu aumento foi de R${Aumento}'
                     f'\n O seu novo salário é: R$ {SalarioAjustado}')

    else:
        Percentual = 0.05
        Aumento = SalarioAtual * Percentual
        SalarioAjustado = SalarioAtual + Aumento
        return print(f'O seu antigo salário era: R$ {SalarioAtual}'
                     f'\nO seu reajuste foi de: {Percentual*100}%'
                     f'\nO seu aumento foi de R$ {Aumento}'
                     f'\nO seu novo salário é: R$ {SalarioAjustado}')
# print(exec28(200))


"""
29 - Faça um programa para o cálculo de uma folha de pagamento
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade
de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220
"""


def exec29(Horas, SalHora):
    Bruto = Horas * SalHora
    Bruto = round(Bruto)
    Fgts = 0.11
    Sindicato = 0.03

    if(Bruto <= 900):
        return 'Isento'
    elif(Bruto > 900 and Bruto <= 1500):

        Ir = 0.05
        Inss = 0.10
        desconto = (Bruto * Ir) + (Bruto * Sindicato) + (Bruto * Inss)
        Liq = Bruto - desconto
        print(f'Salário Bruto: {Horas} * {SalHora} : R${Bruto}'
              f'\n(-) IR (%{Ir*100}) : R$ {Ir*Bruto} '
              f'\n(-) INSS (%{Inss*100}) : R$ {Inss*Bruto}'
              f'\nFGTS (%{Fgts*100}) : R$ {Fgts*Bruto}'
              f'\nO sindicato cobra: R$ {Bruto*Sindicato}'
              f'\nTotal de descontos: {desconto}'
              f'\nSalário liquido R${Liq}')

    elif(Bruto > 1500 and Bruto <= 2500):
        Ir = 0.10
        Inss = 0.10
        Liq = Bruto - (Sindicato + (Bruto * Inss) + (Bruto * Ir))
        print(f'Salário Bruto: {Horas} * {SalHora} : R${Bruto}'
              f'\n(-) IR(%{Ir*100}) : R$ {Ir*Bruto} '
              f'\n(-) INSS (%{Inss*100}) : R$ {Inss*Bruto}'
              f'\nFGTS (%{Fgts*100}) : R$ {Fgts*Bruto}'
              f'\nTotal de descontos: {Ir*Bruto+Sindicato*Bruto+Inss*Bruto}'
              f'\nSalário liquido R${Liq}'
              )
    elif(Bruto > 2500):
        Ir = 0.20
        Inss = 0.10
        Liq = Bruto - (Sindicato + (Bruto * Inss) + (Bruto * Ir))
        print(f'Salário Bruto: {Horas} * {SalHora} : R${Bruto}'
              f'\n(-) IR(%{Ir*100}) : R$ {Ir*Bruto} '
              f'\n(-) INSS (%{Inss*100}) : R$ {Inss*Bruto}'
              f'\nFGTS (%{Fgts*100}) : R$ {Fgts*Bruto}'
              f'\nTotal de descontos: {Ir*Bruto+Sindicato*Bruto+Inss*Bruto}'
              f'\nSalário liquido R${Liq}'
              )


#print(exec29(5, 1220))

"""
30 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
def exec30(dia):

    if(dia == 1):
        return 'DominGo'
    elif(dia == 2):
        return 'Segunda-Feira'
    elif(dia == 3):
        return 'Terca-Feira'
    elif(dia == 4):
        return 'Quarta-Feira'
    elif(dia == 5):
        return 'Quinta-Feira'
    elif(dia == 6):
        return 'Sexta-Feira'
    elif(dia == 7):
        return 'Sabado'
    else:
        return 'Numero invalido'

# print(exec30(13))


"""
32 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

"""


def exec32(n1, n2):
    media = (n1 + n2) / 2
    if(media >= 9 and media <= 10):
        return f'Conceito: A {media} \nAprovado'
    elif(media >= 7.5 and media < 9):
        return f'Conceito: B {media} \nAprovado'
    elif(media >= 6 and media < 7.5):
        return f'Conceito: C {media} \nAprovado'
    elif(media >= 4 and media < 6):
        return f'Conceito: D {media} \nReprovado'
    elif(media >= 0 and media < 4):
        return f'Conceito: E {media} \nReprovado'


`
#print(exec32(4, 8))


"""
33 - Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois
lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""
def exec33(l1, l2, l3):


"""
34 - Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
def exec34()

"""
35 -
"""


"""
36 -
"""


"""
37 -
"""


"""
38 -
"""

"""
39 -
"""

"""
40 -
"""
