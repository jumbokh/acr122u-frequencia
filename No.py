#!/usr/bin/env python
# -*- coding: utf-8 -*-


class No(object):
    tipo = None
    numLinha = None
    pais = []
    coberto = False

    def __init__(self, tipo, numLinha):
        self.tipo = tipo
        self.numLinha = numLinha

    def setPai(self, pais):
        if (isinstance(pais, int)):
            self.pais.append(pais)
        elif (isinstance(pais, list)):
            while (len(pais) > 0):
                self.pais.append(pais.pop())

    def setCoberto(self):
        self.coberto = True

    def getTipo(self):
        return self.tipo

    def getNumLinha(self):
        return self.numLinha

    def getPais(self):
        return self.pais

    def getCoberto(self):
        return self.coberto
