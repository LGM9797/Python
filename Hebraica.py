import psycopg2 as pg
import sys

# Insira aqui o nome dos bancos de dados que deseja monitorar:
dbnames = ['csbrasil', 'vb3', 'delrey', 'saojudas', 'elux', 'viacaoitu', 'caxanga', 'vbtransportes', 'softbus',
           'rapidocampinas', 'viacaocampodosouros', 'viasudeste',
           'grupobelarminohortolandia', 'jslsjc', 'mobipe', 'pirajucarakdb', 'sambaiba', 'estre', 'alliancetruckparts',
           'barata', 'ribeiraopreto', 'veoliasp', 'metropolekdb', 'estretaboaokdb',
           'realalagoaskdb', 'metropolitanakdb', 'saofranciscokdb', 'cidadealtakdb', 'braspress', 'gbvalinhos',
           'gbsantacruz', 'veolia', 'estrecuritiba', 'estrecampolargo', 'kontrow',
           'danubioazul', 'csbrasilkdb', 'gpkdb', 'mobibrasilsp', 'grajaukdb', 'jtukdb', 'vcm', 'vcgkdb',
           'viacaojacareikdb', 'miracatibakdb', 'mgmrental', 'norbrasil', ]


txt = open('matriz.txt', 'w', encoding='utf-8')  # localização do arquivo txt que será preenchido
host = '10.100.1.12'  # Host da conexão (obs: deve estar conectado via VPN)
port = '5432'
user = 'postgres'
password = 'postgre'
tbname = 'devices'  # Nome da tabela

def produzidosVSativos(lista):  # função que realiza o relatório de produzidos x ativos
    for i in lista:  # percorre todos os bancos da lista dbnames
        dbname = i
        connection = pg.connect(
            "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(host, port, dbname, user, password))

        cur = connection.cursor()
        cur.execute("select count(*) from devices where status = 6")
        out1 = dbname, ';', 'Disponiveis para instalação;', cur.fetchall().pop(0), ';'
        print(out1)
        txt.write(str(out1) + '\n')

        cur = connection.cursor()
        cur.execute("select count(*) from devices where status = 8")
        out2 = dbname, ';', 'Ativos;', cur.fetchall().pop(0), ';'
        print(out2)
        txt.write(str(out2) + '\n')  # #função que re

produzidosVSativos(dbnames)


