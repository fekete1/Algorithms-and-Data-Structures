from Ngrama import *
from ListaEncadeada import *
import numpy as np
import string

def remove_pontuacao(texto):
    '''
    Remove todas as pontuações de uma texto.
    '''
    aux = ''
    for x in texto:
        if x not in string.punctuation:
            aux+= x
    return aux

def arquivo_em_vetor(nome_arquivo):
    '''
    Recebe o nome do arquivo de texto, criando um vetor que possui cada palavra desse texto.
    '''
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    texto = texto.replace('\n',' ').replace('\t',' ').lower().split(' ')
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
        return str(tuple(self.__palavras))
    
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

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo
    
    @property
    def palavras(self):
        return self.__palavras
