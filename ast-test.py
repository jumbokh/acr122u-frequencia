#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import ast
from graphviz import Digraph
from Grafo import Grafo


def foo(a):  # função a ser testada
    b = 2 + a
    if (b > 2):
        print a
        print b
    else:
        print a
        print "asfsad"
        a = 123
        b = 234
    pass


# subclasse do método da ast para visitar os nós
class SimpleVisitor(ast.NodeVisitor):

    def __init__(self):
        self.nodeList = []
        self.anteriorNode = 1
        dot.node('1', "root")

    def graphNodeSetter(self, nodeType):
        """Cria os nós do grafo, ainda falta implementar a parte de agrupar
        todos os que não alterarem o fluxo e estiverem em sequência."""
        dot.node(str(self.anteriorNode + 1), nodeType)
        self.graphEdgeSetter(nodeType)
        self.anteriorNode = self.anteriorNode + 1

    # cria as arestas (bem rudimentar ainda, só pra testar)
    def graphEdgeSetter(self, nodeType):
        # if (nodeType=="assignment"):
        dot.edge(str(self.anteriorNode), str(self.anteriorNode + 1))

    """Ao definir um método seguindo essa fórmula: visit_NomeDaClasseDaAst,
    define-se o que vai ser feito ao visitar um nó dessa classe."""

    def visit_Module(self, node):
        # asts sempre iniciam com módulo, coloquei ele chamando o resto
        self.generic_visit(node)
        print "\nLista dos nós ignorados:\n", self.nodeList

    def visit_Assign(self, node):
        self.graphNodeSetter("assignment")

    def visit_arguments(self, node):
        pass

    def visit_If(self, node):
        """Todo If tem os parâmetros test(condição),
        body(condição satisfeita) e orelse(condição não satisfeita).
        os nós correspondentes a esses campos ficam dentro deles"""

        self.graphNodeSetter("if")
        print "\nIF: BLOCOS:"
        print "test: ", node.test
        # self.generic_visit(node.test)
        print "body: ", node.body
        for no in node.body:
            self.visit(no)
        print "orelse: ", node.orelse, "\n"
        for no in node.orelse:
            self.generic_visit(no)  # se chamar generic, fura as restrições
        # o foco está sendo aqui

    def generic_visit(self, node):
        """Classes cuja visita não tiver sido redefinida
        pelos métodos acima serão visitadas por esse método."""

        # o que ainda não foi pego pelas classes
        print len(self.nodeList), ".", type(node).__name__  # printa o tipo

        self.nodeList.append(node)
        ast.NodeVisitor.generic_visit(self, node)  # chamando a visita original


dot = Digraph(comment='AST NODES')

print "CODIGO DA FUNCAO:"
print inspect.getsource(foo)

simple_visitor = SimpleVisitor()
astOfSource = ast.parse(inspect.getsource(foo))

print "\n\nPRINTANDO A AST INTEIRA:"
print ast.dump(astOfSource)

print "\n\nUSANDO A SimpleVisitor:"
simple_visitor.visit(astOfSource)

print "\n\nSource do .DOT"
print dot.source
# dot.render('teste-grafo/grafo.gv', view=True)  # salva o grafo e o exibe
