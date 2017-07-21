#!/usr/bin/env python
# -*- coding: utf-8 -*-
from No import No


class Grafo:
    """Gera um grafo cujos nós vão sendo
    definidos a partir de seu tipo, número de linha,
    etc.
    para gerar o .dot, faz-se uma busca em profundidade
    reversa (tem nome pra isso?) partindo dos nós sem filhos
    ou de nós de retorno e percorrendo por seus pais.

    """

    numNos = 0
    listaNos = []
    listaSemFilhos = []  # para usar como pais do nó seguinte ao orelse
    listaReturn = []
    pilhaIf = []
    anterior = None
    campo = None  # define se está no body ou orelse de um if

    def __init__(self):
        pass

    def verificador(self, tipo):
        """
        Verifica se o nó desvia o fluxo.

        Por enquanto, o if que lida com isso de alterar o fluxo só
        verifica se o nó é do tipo If.

        Retorna True caso desvie o fluxo.
        """

        if (self.anterior is None):  # se for o primeiro nó do grafo, o cria
            return True
        if (tipo is not "If" and self.anterior.getTipo() is not "If"):
            return False
        return True

    def defCampo(self, campo):  # define o contexto do próximo nó
        self.campo = campo  # pode ser body, orelse, fimOrelse, etc.

    def defPai(self, no):
        """
        Quando for o primeiro elemento do orelse, define o pai dele
        como o if mais recente da pilha e desempilha esse if.

        Quando for o primeiro elemento depois de um orelse, define
        seus pais como sendo todos os nós sem filhos (que não são return).

        Caso contrário, define o pai como sendo o nó anterior.
        """
        if (self.campo == "orelse"):
            no.setPai(self.pilhaIf.pop())
            self.defCampo(None)

        elif (self.campo == "fimOrelse"):
            lista = []

            # esvazia a lista de nós sem filhos e coloca todos como pais do nó
            while (len(self.listaSemFilhos) > 0):
                lista.append(self.listaSemFilhos.pop())
            no.setPai(lista)
        else:
            no.setPai(self.anterior)

    def criaNo(self, tipo, numlinha):
        """
        Cria nó apenas se ele mudar o fluxo do programa, para que
        não se repitam nós seguidos que não alterem o fluxo;
        para duas atribuições seguidas, por exemplo, será criado
        apenas um nó.
        """

        if (not self.verificador(tipo)):
            pass  # se não altera fluxo, ignora nó da ast e não cria no grafo
        else:
            no = No(tipo, numlinha)
            self.numNos += 1
            self.listaNos.append(no)
            if (tipo == "If"):
                self.pilhaIf.append(no)
            if (tipo == "Return"):
                self.listaReturn.append(no)
            # Definir os outros tipos aqui.

            self.defPai(no)
            self.anterior = no  # nó recém incluido é anterior ao próximo

    def printGrafo(self):
    	for no in listaNos:
    		print no.getTipo(), " Filho de: "
    			for pai in no.getPais():
    				print pai, ", "


grafo = Grafo()
for n in range(1,5):
	print n
	criaNo("If", n)

printGrafo()