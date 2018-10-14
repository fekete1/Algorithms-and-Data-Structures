'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.com.br)
Centro de Informatica (CIn) (http://www.cin.ufpe.br)
IF969 - Algoritmos e Estrutura de Dados

Autor: José Sheldon Brito Fekete (jsbf)
Email: jsbf@cin.ufpe.br
Data: 2018-10-14
'''

import os
from ListaEncadeada import *
from Documento import *

def diretorio_em_lista():
    '''
    Itera pelo diretório dos arquivos de textos, transformando-os em objetos da classe Documento,
    em seguida os insere em uma lista encadeada
    '''
    
    caminho = os.getcwd()
    pasta = '\dados\src'
    lista_arquivos = ListaDuplamenteEncadeada()
    for p, d, files in os.walk(caminho+pasta):
        for f in files:
            temp = Documento(caminho+pasta+'\\'+f)
            temp.nome_arquivo = f
            lista_arquivos.anexar(temp)
    return lista_arquivos
            
def ordenacao(ld,lc):
    '''
    Ordena os documentos por contenção em ordem decrescente.
    Essa ordenação procura a maior contenção entre os documentos, quando a acha
    apaga tanto o documento quanto a contenção das listas antigas, colocando em listas
    novas ordenadas.
    '''
    ld_ordenada = ListaDuplamenteEncadeada()
    lc_ordenada = ListaDuplamenteEncadeada()

    
    
    while len(lc) > 0:
        maior_index = 0
        for index in range(0,len(lc)):
            if lc[index] > lc[maior_index]:
                maior_index = index
                
        ld_ordenada.anexar(ld[maior_index])
        lc_ordenada.anexar(lc[maior_index])
        ld.remover(ld[maior_index])
        lc.remover(lc[maior_index])
    return ld_ordenada, lc_ordenada
        

class Corpus(object):
    '''
    Classe responsável por armazenar um conjunto de documentos de texto de um determinado
    diretório
    '''
    def __init__(self):
        self.__corpus = diretorio_em_lista()

    def __str__(self):
        '''
        O objeto quando transformado em string ou for printado irá retornar
        a lista de documentos armazenados nele
        '''
        return str(self.corpus)
    
    def __repr__(self):
        return 'Corpus()'
        
    
    def __len__(self):
        '''
        Retorna quantos documentos de texto o objeto está armazenando.
        '''
        return len(self.__corpus)
        
    def verificarPlagio(self,documento,limiar):
        '''
        É passado um documento e a limiar de contenção, será verificado a contenção do documento
        passado em todos os documentos de texto armazenados no objeto, após isso será
        retornado os documentos que são mais provaveis de terem sidos plagiados, apenas os
        documentos que ultrapassaram a limiar de contenção serão exibidos
        '''
        
        lista_documentos = ListaDuplamenteEncadeada()
        lista_contencao = ListaDuplamenteEncadeada()
        
        for texto in self.__corpus:
            contencao = documento.contencao(texto)
            if contencao >= limiar:
                lista_documentos.anexar(texto)
                lista_contencao.anexar(contencao)
        documentos_plagiados,qtde_contencao = ordenacao(lista_documentos, lista_contencao) #Retorna apenas os documentos.
        return documentos_plagiados
                
            
    
    @property
    def corpus(self):
        return self.__corpus
