#String eh uma sequencia de caracteres. Serve p trabalhar com texto
"""
sobreMim = 'Meu nome eh Lucas monteiro tenho 23'
meuNome = 'Lucas'
subString = meuNome[0:len(meuNome)-2] #toda string eh uma lista| [:] fatiamento
#print(subString)
subSobreMim = sobreMim[-2:]
print(subSobreMim)
"""




#
# index = url.find('=') #
# print(index)
# real = url[index +1:]
# print(real)
# listaArgs = url.split('=')
# print(listaArgs)

# print(url[index + 1:])
# print(listaArgs[0:2])
#
# separandoNome = nomeArquivo.split('_')
# print(separandoNome)
# print(separandoNome[:-1])
# #nomeArquivo = separandoNome[:-1]
# print(nomeArquivo)
# nomeArquivo = nomeArquivo[:]
# print(nomeArquivo)

nomeArquivo = 'Alternador_Report_GatoPreto_GP-3_06Julho_a_12julho2020_ijhbd31244d'
url = 'https://www.bitebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
urlVazia = None

from ExtratorArgumentos import ExtratorArgumentos

# arg = ExtratorArgumentos.valorValido(url)
# print(arg)

nome = ExtratorArgumentos(nomeArquivo)
#print(nome.valor)
novoNome = nome.ExtraiArgumentos()
print(f'nome antigo: {nome.valor} '
      f'\nnovo nome: {novoNome}')




