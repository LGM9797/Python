from Classes import LimpadorNome
import os

path = '/Users/lucasmonteiro/Desktop/GP1/'
oldName = os.listdir(path)[1]

nome = LimpadorNome(oldName, path)
newName = nome.ExtraiArgumentos()

oldName = path+oldName

os.rename(oldName, newName) #Args os.rename(old,new)
