"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.com.br)
Centro de Informatica (CIn) (http://www.cin.ufpe.br)
IF969 - Algoritmos e Estrutura de Dados

Autor: José Sheldon Brito Fekete (jsbf)
Email: jsbf@cin.ufpe.br
Data: 2018-09-16

Copyright(c) 2018 José Sheldon Brito Fekete
"""

class No:
    '''
    Objeto do tipo Nó, cada nó irá armazenar o valor do mesmo, a referência do nó posterior e o nó anterior.
    '''
    def __init__(self,dado=None,prox=None,ante=None):
        '''
        Construtor do objeto Nó
        '''
        self.dado = dado
        self.prox = prox
        self.ante = ante


class ListaDuplamenteEncadeada:
    '''
    Classe do tipo lista duplamente encadeada, os nós possuem a referencia do nó anterior e nó posterior.
    '''
    
    def __init__(self,conteudo=()):
        '''
        Recebe o conteudo e cria um objeto do tipo ListaDuplamenteEncadeada, se o conteudo for vazio, as referencias do primeiro e ultimo serão
        iguais e a lista será vazia, se for umobjeto iteravel, ele irá passar por cada parte do mesmo, criando um nó e adicionando-os no final da lista.
        '''
        
        self.primeiro = self.ultimo = No()
        self.tamanho = 0

        for valor in conteudo:
            self.anexar(valor)
        
    
    def anexar(self,dado):
        '''
        Recebe um valor, criando um nó e adicinando-o no final da lista.
        '''
        
        novoNo = No(dado,None,self.ultimo)
        self.ultimo.prox = novoNo
        self.ultimo = novoNo
        self.tamanho +=1

    def inserir(self,index,valor):
        '''
        Recebe o valor e o índice onde o nó ira ser inserido, criando o nó e inserindo ele na
        posição determinada
        '''
        if index >= self.tamanho -1:
            self.anexar(valor)
        elif index < 0:
            raise IndexError
        else:
            novoNo = No(valor)
            posterior = self.__getitem__(index,"privado")
            anterior = posterior.ante
            
            novoNo.ante = anterior
            anterior.prox = novoNo
            
            novoNo.prox = posterior
            posterior.ante = novoNo
            self.tamanho +=1

    def estender(self,conteudo):
        '''
        Recebe um objeto iterável, adicionando seus elementos no final da lista duplamente encadeada.
        '''
        
        for valor in conteudo:
            self.anexar(valor)

    def trocar(self,primeiro,segundo):
        '''
        Recebe o indice dos dois elementos e troca os valores dos mesmos. 
        '''
        
        self[primeiro], self[segundo] = self[segundo],self[primeiro]
        
    def copiar(self):
        '''
        Copia o conteudo da lista atual e retorna o mesmo.
        '''
        
        return ListaDuplamenteEncadeada(self)

    def procurar(self,valor):
        '''
        Recebe o valor do nó e retorna o indice do mesmo.
        '''

        cont = 0
        for elemento in self:
            if elemento == valor:
                return cont
            cont+=1
        raise IndexError

    def tirar(self,index=None):
        '''
        Remove o elemento de indice pesquisado da lista, ou se não foi passado o indice, removerá o ultimo elemento,
        e então retorna o elemento removido.
        
        '''
        if len(self) == 0:
            return None
        
        #Entrara aqui nos casos de não passar o indice e de passar o indice do ultimo elemento
        #Ele trocará a referência do ultimo para o anterior do elemento deletado
        if index is None or index == len(self) -1:
            index = len(self) - 1
            atual = self.__getitem__(index,"privado")
            anterior = self.__getitem__(index,"privado").ante

            aux = atual.dado
            anterior.prox = None
            self.ultimo = anterior
            
            del atual
            self.tamanho -=1

            return aux
        
        
        atual = self.__getitem__(index,"privado")
        anterior = self.__getitem__(index,"privado").ante
        posterior = self.__getitem__(index,"privado").prox

        aux = atual.dado
        anterior.prox = atual.prox
        posterior.ante = atual.ante
        
        del atual
        self.tamanho -=1
        return aux

    def remover(self,valor):
        '''
        Remove o nó da lista de acordo com o valor passado, e só remove a primeira
        ocorrencia daquele valor.
        '''
        for index, elemento in enumerate(self):
            if elemento == valor:
                if index == len(self) -1:
                    atual = self.__getitem__(index,"privado")
                    anterior = self.__getitem__(index,"privado").ante

                    aux = atual.dado
                    anterior.prox = None
                    self.ultimo = anterior
                    
                    del atual

 
                else:
                    atual = self.__getitem__(index,"privado")
                    anterior = self.__getitem__(index,"privado").ante
                    posterior = self.__getitem__(index,"privado").prox

                    aux = atual.dado
                    anterior.prox = atual.prox
                    posterior.ante = atual.ante

                    del atual
                break

        self.tamanho -=1

    def eliminar(self,valor):
        pass
 
  
                    
    def __str__(self):
        '''
        Configura como a objeto será vizualizado quando for printado ou transformado em string.
        '''
        
        if self.tamanho ==0:
            return "[]"
        aux = self.primeiro
        string = ""
        string +='['
        while aux.prox is not None:
            aux=aux.prox
            if type(aux.dado) is str:
                string += '"'
                string += str(aux.dado)
                string += '"'
            else:
                string += str(aux.dado)   
            string += '; '
        string = string[:-2]
        string +=']'
        return string
    
    def __repr__(self):
        '''
        Configura a reprodução do objeto, retornando uma forma válida para instanciar o mesmo.
        '''
        
        return 'ListaDuplamenteEncadeada '+str(self)
        
    def __iter__(self):
        '''
        Cria um apontador e determina como ele irá ser percorrido pela keyword 'for'
        '''
        return self.Iterador(self)

    
    def __getitem__(self,index,check="publico"):
        '''
        Irá determinar os indices dos nós da lista e retornar o valor do mesmo quando for chamado por um usuário comun.
        Quando for chamado pela função for chamada pelo programador (reutilizando linhas de código) ela ira retornar a refêrencia do nó
        '''
        
        if index < 0 or index >= self.tamanho:
            raise IndexError()
        
        cont = 0
        #O usuário comun não irá chamar a função '__getitem__' e sim usar a formula dela (ex: objeto[0]), então a função terá sempre o atributo check em publico
        if check is 'publico':
            for item in self:
                if cont == index:

                    return item
                cont += 1
        else:
            aux = 0
            aux_ref = self.primeiro.prox
            while aux < index:
                aux_ref = aux_ref.prox
                aux += 1
            return aux_ref

  
    def __setitem__(self, index, valor):
        '''
        Recebe o index do nó e o valor, atualizando o valor do nó.
        Utilizei o metodo ''__getitem__'' pós ele retorna a referência do nó e consegue atualizar os valores do mesmo,
        usando o getitem publico (ex: lista[index] = valor) ele iria retornar o dado do nó e não a referência.
        '''
        
        self.__getitem__(index,"privado").dado = valor

    def __len__(self):
        '''
        Retornar o tamanho da Lista Duplamente Encadeada.
        '''
        
        return self.tamanho

    def __contains__(self,valor):
        '''
        Verifica se o valor passado existe na lista duplamente encadeada.
        '''
        
        for elementos in self:
            if elementos == valor:
                return True
        return False
                
        

    class Iterador:
        '''
        Classe do tipo iterador, define do irá ser percorrido os elementos no objeto Lista Duplamente Encadeada
        '''
        
        def __init__(self,lista):
            '''
            Construtor da classe Iterador
            '''
            self.__ponteiro = lista.primeiro.prox


        def __next__(self):
            '''
            Ele determina que quando for chamado a keyword 'for' o objeto será percorrido do primeiro elemento
            até o ultimo seguindo a ordem referencial.
            '''
            try:
                aux = self.__ponteiro.dado
                self.__ponteiro = self.__ponteiro.prox
                return aux
            except:
                raise StopIteration()

def concatenar(listaUm, listaDois):
    '''
    Concatena as duas linhas passadas como parametro
    '''
    listaGeral = listaUm.copiar()
    listaGeral.estender(listaDois)
    return listaGeral
