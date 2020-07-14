# -*- coding: utf-8 -*-

from Conta import *

conta1 = Conta(123, 'lucas', 100, 100)
conta2 = Conta(113, 'luis', 120, 140)


# conta1.extrato()
# conta2.extrato()
# conta1 = None -> Apaga a referencia entre a variavel e o objeto
# conta1.extrato() Após apagar a referencia, nao existe mais esse endereco


"""from datas import DataFormat

data = DataFormat(20, 5, 1997)
data.formatada()
"""
# conta1.transferencia(15, conta2)
# conta1.extrato()
# conta2.extrato()
# conta1.set_limite(1500)
# print(conta1.get_limite())

print(conta1.limite)
conta1.limite = 150
print(conta1.limite)
print(conta1.saldo)

conta1.saque(250.5)
print(Conta.codBanco())
codigo = Conta.codBanco()
print(codigo['BB'])

conta1 = None
conta2 = None
