# -*- coding: utf-8 -*-

import random

from abc import ABC #abstract base classes
from _collections_abc import MutableSequence

class Programa:  # Classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()  # Title() deixas todas as primeiras letras maiusculas
        self.ano = ano
        self._likes = 0

    def AddLike(self):
        self._likes += 1

    @property
    def ExibirLikes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):  # Imprime todos os valores herdados e da classe atual
        return f'{self._nome} - {self.ano} - Likes: {self._likes}'


class Filme(Programa):  # Classe filha (herdando atributos e metodos da classe mãe)

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Criando um objeto da classe mãe dentro da classe filha
        self.duracao = duracao

    def __str__(self):  # Imprime todos os valores herdados e da classe atual
        return f'{self._nome} - {self.ano} - {self.duracao} mins - Likes: {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # Imprime todos os valores herdados e da classe atual
        return f'{self._nome} - {self.ano} - {self.temporadas} temps - Likes: {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  # ganha comportamentos na classe (duckTypping) do tipo list"
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


class Playlist2(MutableSequence):
    pass


filme1 = Filme('Kill Bill', 2004, 120)
serie1 = Serie('The Boys', 2020, 1)
filme2 = Filme('lotr', 2003, 250)
serie2 = Serie('GOT', 2009, 8)

for i in range(0, random.randint(1, 100)):
    filme1.AddLike()
    filme2.AddLike()

for i in range(0, random.randint(1, 100)):
    serie1.AddLike()
    serie2.AddLike()

FilmesSeries = [filme1, serie1, filme2, serie2]

Playlist_fds = Playlist('FDS', FilmesSeries)

for programa in Playlist_fds:
    print(programa)

print(f'Tamanho playlist {len(Playlist_fds)}')
print(f'Esta ou nao {serie2 in Playlist_fds}')
print(f'Imprimindo o primeiro item da lista {Playlist_fds[0]} ')
