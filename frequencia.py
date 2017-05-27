#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from datetime import date
from smartcard.scard import *


#REMOVIDOS POR NÃO SER EFICAZ LANÇAR ONLINE DIRETO (LEVA TEMPO E A AUTENTICAÇÃO EXPIRA DEPOIS DE ALGUNS MINUTOS DE EXECUÇÃO)
"""
def cadastraCodigo(colunaMatriculas, colunaCodigos):
	a = 0
	print "CADASTRAR CODIGO"	
	presenca = raw_input("Lancar presenca apos cadastrar? (S/n): ")
	presenca = presenca.upper()
	
	if presenca != "N":
		presenca = True
	else:
		presenca = False
	
	while True:
		while True:
			try:
				matricula = raw_input("Digite sua matricula: ")
				matricula = matricula.upper() #maiuscula
				a = sheet.find(matricula)
				if a.col != colunaMatriculas:
					print "Matricula nao encontrada"
				else:
					print "Matricula encontrada"
					break
			
			except (gspread.exceptions.CellNotFound):
				print "Matricula nao encontrada"
			
			except (NameError):
				print "Sistema offline. Utilizar cadastraOffline"
				break		
		linha = a.row
		codigo = leCodigo()		
		sheet.update_cell(linha, colunaCodigos, codigo)
		print "Codigo cadastrado\n"
		if presenca:
			lancaPresenca(str(codigo))
		print "CADASTRAR CODIGO"	
"""

""" 
def lancaPresenca(codigo = False): #parametro pra poder chamar do cadastro
	dia = obtemDia()
	breaksoon = False
	
	if codigo != False:	
		breaksoon = True
	
	while True:
		print "\nLANCAR PRESENCA"
		if (breaksoon == False):
			codigo = str(leCodigo())
		print "Buscando codigo na planilha"
		
		try:
			coluna = sheet.find(dia).col
			linha = sheet.find(codigo).row
		
		except (gspread.exceptions.CellNotFound):
			print "Codigo ou dia invalido"
		
		except (NameError):
			salvaTxtNaoLancadas(codigo, dia)
			print "Presenca lancada no txt"
			print "Presenca NAO lancada na planilha"

		else:
			salvaTxtLancadas(codigo, dia)
			print "Presenca lancada no txt"
			sheet.update_cell(linha, coluna, 1)
			print "Presenca lancada na planilha\n"
		
		if breaksoon:
			break
		again = raw_input("Inserir outra? (S/n): ")
		again = again.upper()
		if again == "N":
			break
"""



def codigoParser(codigo):
	codigoParsed = 0
	for i in range(0,6):
		codigoParsed += codigo[i]*(pow(10,3*(5-i)))
	return hex(codigoParsed)


def leCodigo(): 
	print "Insira o cartao"
	
	while True:
		
		try:
			hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
			assert hresult==SCARD_S_SUCCESS
			hresult, readers = SCardListReaders(hcontext, [])
			assert len(readers)>0
			reader = readers[0]
			hresult, hcard, dwActiveProtocol = SCardConnect(
			    hcontext,
			    reader,
			    SCARD_SHARE_SHARED,
			    SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
			hresult, response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xCA,0x00,0x00,0x00])
			assert len(response) == 6
			print "Cartao detectado"
			return codigoParser(response)
		except KeyboardInterrupt:
			raise
		except:
			pass
		
		time.sleep(0.5)

def leCodigoStub(): #usado para testes sem leitor
	a = [243,43,43,23,12,43]
	return codigoParser(a)


def cadastraOffline():
	dia = obtemDia()
	with open("cadastrar/cadastro.txt", 'a') as file:
		while True:		
			print"\nCADASTRAR CARTAO"
			proximo = raw_input("aperte ENTER para CADASTRAR E LANCAR PRESENCA, digite PRES para SOMENTE PRESENCA:\n")
			proximo = proximo.upper()
			if (proximo=="PRES"):
				return(-1)	
			matricula = raw_input("Digite sua matricula: ")
			matricula = matricula.upper()
			codigo = leCodigoStub()
			file.write(matricula + ":"+ str(codigo) + ":" + dia + "\n")
			print "cadastro offline concluido\n"


def lancaPresencaOffline():
	dia = obtemDia()		
	while True:
		print "\nLANCAR PRESENCA"	
		proximo = raw_input("aperte ENTER para PRESENCA, digite CAD para CADASTRO:\n")
		proximo = proximo.upper()
		if (proximo=="CAD"):
			return(-2)	
		codigo = str(leCodigoStub())
		salvaTxtNaoLancadas(codigo, dia)
		print "Presenca registrada\n"
		
		

def obtemDia(): #pega o dia e converte pro formato que ta na planilha
	hoje = date.today()
	meses = ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez")
	mes = meses[hoje.month-1]
	hoje = str(hoje.day) + "-" + str(mes)
	return hoje

def salvaTxtLancadas(codigo, dia):
	with open("chamadas/presencas lancadas/"+str(dia)+".txt", 'a') as file:
		file.write(str(codigo)+ "\n")


def salvaTxtNaoLancadas(codigo, dia):
	with open("chamadas/naoLancadas.txt", 'a') as file:
		file.write(str(codigo)+":"+str(dia) + "\n")


### INICIO

operacao = raw_input("Insira a operacao a ser efetuada: \nCADASTRAR OFFLINE = 1 \nPRESENCA OFFLINE = 2:\n")
if operacao == "1":
	shuffle = cadastraOffline()
elif operacao == "2":
	shuffle = lancaPresencaOffline()
#elif operacao == "3":
	#lancaPresenca()
#elif operacao == "4":	
	#cadastraCodigo(colunaMatriculas, colunaCodigos)
else: 
	print "Opcao invalida."
while True:
	if (shuffle == -1):
		shuffle = lancaPresencaOffline()
	elif (shuffle == -2):
		shuffle = cadastraOffline()

	
