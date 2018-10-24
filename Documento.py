# -*- coding: utf-8 -*-

'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.com.br)
Centro de Informatica (CIn) (http://www.cin.ufpe.br)
IF969 - Algoritmos e Estrutura de Dados

Autor: José Sheldon Brito Fekete (jsbf)
Email: jsbf@cin.ufpe.br
Data: 2018-10-14
'''



from Ngrama import *
from ListaEncadeada import *
import numpy as np
import re



def arquivo_em_vetor(nome_arquivo):
    '''
    Recebe o nome do arquivo de texto, criando um vetor que possui cada palavra desse texto.
    filtrando pontuações e quebras de linhas
    '''
    exp = r'[^\w ]{1}'
    exp_quebras = r'\s{1,}'
    
    arquivo = open(nome_arquivo,'r',encoding = 'utf-8')
    texto = arquivo.read()
    texto = re.sub(exp_quebras, ' ', texto)
    texto = re.sub(exp, '', texto)
    texto = texto.lower().split(' ')
    vetor = np.array(texto)
    arquivo.close()
    return vetor
    
   
class Documento(object):
    '''
    Refere a um documento de texto, armazenando as palavras do mesmo em um vetor
    '''
    
    def __init__(self,nome_arquivo):
        self.__nome_arquivo = nome_arquivo
        self.__palavras = arquivo_em_vetor(nome_arquivo)
        
    def __str__(self):
        return str(self.__nome_arquivo)
    
    def __repr__(self):
        return 'Documento'+'("'+self.__nome_arquivo+'")'
    
    def gerarNgramas(self):
        '''
        Transforma um array de strings(entrada) em uma lista encadeada de bigramas(saída)
        '''
        palavras = self.__palavras
        lista = ListaDuplamenteEncadeada()      
        for index in range(0,len(palavras)):
            if index == len(palavras)-2:
                break
            else:
                temp = Ngrama(palavras[index],palavras[index+1],palavras[index+2])
                lista.anexar(temp)
        return lista

    def contencao(self,documento):
        '''
        Verifica a contenção do objeto no documento passado como parâmetro
        '''

        cont = 0
        ngramas_atual = self.gerarNgramas()
        ngramas_documento = documento.gerarNgramas()
        for ngrama in ngramas_atual:
            if ngrama in ngramas_documento:
                cont +=1
                ngramas_documento.remover(ngrama)
        contencao = cont/len(ngramas_atual)
        return contencao
                

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo
    
    @nome_arquivo.setter
    def nome_arquivo(self,novo_nome):
        self.__nome_arquivo = novo_nome
    
    @property
    def palavras(self):
        return self.__palavras
    
    @palavras.setter
    def palavras(self,novas_palavras):
        self.__palavras = novas_palavras
