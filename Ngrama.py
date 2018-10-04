"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.com.br)
Centro de Informatica (CIn) (http://www.cin.ufpe.br)
IF969 - Algoritmos e Estrutura de Dados

Autor: José Sheldon Brito Fekete (jsbf)
Email: jsbf@cin.ufpe.br
Data: 2018-10-02

Copyright(c) 2018 José Sheldon Brito Fekete
"""

import numpy as np

class Ngrama(object):
    '''
    A classe Ngrama representa uma subsequência de N palavras de um certo texto.
    '''
    
    def __init__(self,*palavras):
        self.__ngrama = np.array(palavras)
        self.__tamanho = self.__ngrama.size
    
    def __str__(self):
        return str(tuple(self.__ngrama))


    def __repr__(self):
        return 'Ngrama'+str(tuple((self.__ngrama)))

        
    def __len__(self):
        return self.__tamanho
    
    
    def __eq__(self,outro):
        return str(self) == str(outro)

    @property
    def ngrama(self):
        return self.__ngrama
