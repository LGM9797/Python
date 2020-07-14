from Classes import LimpadorNome
import os

path = '/Users/lucasmonteiro/Desktop/GP1/'
print(os.listdir(path))

for arquivos in os.listdir(path):
    if(arquivos != '.DS'):
        oldName = arquivos
        nome1 = (LimpadorNome(arquivos, path))
        nome1 = nome1.ExtraiArgumentos()
        oldName1 = path+oldName
        os.rename(oldName1, nome1)





