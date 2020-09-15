from Classes import LimpadorNome
import os

path = r"C:\Users\Lucas Monteiro\Desktop\GP-3/"
path2 = r"C:\Users\Lucas Monteiro\Desktop\GP-1/"

for arquivos in os.listdir(path):
    #if(arquivos != '.DS'):
    oldName = arquivos
    nome1 = (LimpadorNome(arquivos,path))
    nome1 = nome1.ExtraiArgumentos()
    oldName1 = path+oldName
    os.rename(oldName1, nome1)

for arquivos in os.listdir(path2):
    #if(arquivos != '.DS'):
    oldName = arquivos
    nome1 = (LimpadorNome(arquivos,path2))
    nome1 = nome1.ExtraiArgumentos()
    oldName1 = path2+oldName
    print(oldName1)
    os.rename(oldName1, nome1)
    print(nome1)
