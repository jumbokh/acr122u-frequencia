#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from datetime import date
from smartcard.scard import *
from random import randint


def codigoParser(codigo):
    # pega a lista que o leitor retorna e converte pra um número hexadecimal
    codigoParsed = 0
    for i in range(0, 6):
        codigoParsed += codigo[i] * (pow(10, 3 * (5 - i)))
    return hex(codigoParsed)


def leCodigo():
    print "Insira o cartao"

    while True:

        try:
            hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
            assert hresult == SCARD_S_SUCCESS
            hresult, readers = SCardListReaders(hcontext, [])
            assert len(readers) > 0
            reader = readers[0]
            hresult, hcard, dwActiveProtocol = SCardConnect(
                hcontext,
                reader,
                SCARD_SHARE_SHARED,
                SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
            hresult, response = SCardTransmit(hcard, dwActiveProtocol,
                                              [0xFF, 0xCA, 0x00, 0x00, 0x00])
            assert len(response) == 6
            print "Cartao detectado"
            return codigoParser(response)
        except KeyboardInterrupt:
            raise
        except:
            pass

        time.sleep(0.5)


def leCodigoStub():  # usado para testes sem leitor
    a = [randint(0, 255), randint(0, 255), randint(0, 255),
         randint(0, 255), randint(0, 255), randint(0, 255)]
    return codigoParser(a)


def cadastraOffline():
    dia = obtemDia()
    with open("cadastrar/cadastro.txt", 'a') as file:
        while True:
            print"\nCADASTRAR CARTAO"
            matricula = raw_input("Digite sua matricula para CADASTRAR"
                                  " E LANCAR PRESENCA,\n"
                                  "Digite PRES para SOMENTE PRESENCA:\n")
            matricula = matricula.upper()
            if (matricula == "PRES"):
                return(-1)
            codigo = leCodigo()  # trocar por leCodigoStub pra teste s/ leitor
            file.write(matricula + ":" + str(codigo) + ":" + dia + "\n")
            print "cadastro offline concluido\n"


def lancaPresencaOffline():
    dia = obtemDia()
    while True:
        print "\nLANCAR PRESENCA"
        proximo = raw_input("aperte ENTER para PRESENCA,"
                            " digite CAD para CADASTRO:\n")
        proximo = proximo.upper()
        if (proximo == "CAD"):
            return(-2)
        codigo = str(leCodigo())  # trocar por leCodigoStub pra teste s/ leitor
        salvaTxtNaoLancadas(codigo, dia)
        print "Presenca registrada\n"


def obtemDia():  # pega o dia e converte pro formato que ta na planilha
    hoje = date.today()
    meses = ("jan", "fev", "mar", "abr", "mai", "jun",
             "jul", "ago", "set", "out", "nov", "dez")
    mes = meses[hoje.month - 1]
    hoje = str(hoje.day) + "-" + str(mes)
    return hoje


def salvaTxtLancadas(codigo, dia):
    with open("chamadas/presencas lancadas/" + str(dia) + ".txt", 'a') as file:
        file.write(str(codigo) + "\n")


def salvaTxtNaoLancadas(codigo, dia):
    with open("chamadas/naoLancadas.txt", 'a') as file:
        file.write(str(codigo) + ":" + str(dia) + "\n")


# INICIO

operacao = raw_input("Insira a operacao a ser efetuada: "
                     "\nCADASTRAR OFFLINE = 1 \nPRESENCA OFFLINE = 2:\n")
if operacao == "1":
    shuffle = cadastraOffline()
elif operacao == "2":
    shuffle = lancaPresencaOffline()
# elif operacao == "3":
    # lancaPresenca()
# elif operacao == "4":
    # cadastraCodigo(colunaMatriculas, colunaCodigos)
else:
    print "Opcao invalida."

# variando de funcionalidade durante a execução
while True:
    if (shuffle == -1):
        shuffle = lancaPresencaOffline()
    elif (shuffle == -2):
        shuffle = cadastraOffline()
