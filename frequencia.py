import gspread
import time
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from smartcard.scard import *

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

def cadastraOffline():
	dia = obtemDia()
	file = open("cadastrar/cadastro.txt", 'a')
	while True:		
		matricula = raw_input("Digite sua matricula: ")
		matricula = matricula.upper()
		codigo = leCodigo()
		file.write(matricula + ":"+ str(codigo) + ":" + dia + "\n")
		print "cadastro offline concluido\n"

def leCodigo(): #falta implementar conversao pra hex, ta devolvendo uma lista
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
			return response
		
		except:
			a=0 #qualquer coisa pra ocupar o except (preguica de ver como lidar com isso)
		
		time.sleep(0.5)

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

def lancaPresencaOffline():
	dia = obtemDia()		
	while True:
		print "\nLANCAR PRESENCA"		
		codigo = str(leCodigo())
		salvaTxtNaoLancadas(codigo, dia)
		print "Presenca registrada\n"
		proximo = raw_input("aperte ENTER para inserir")
		


def obtemDia(): #pega o dia e converte pro formato que ta na planilha
	hoje = date.today()
	meses = ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez")
	mes = meses[hoje.month-1]
	hoje = str(hoje.day) + "-" + str(mes)
	return hoje

def salvaTxtLancadas(codigo, dia):
	file = open("chamadas/presencas lancadas/"+str(dia)+".txt", 'a')
	file.write(str(codigo)+ "\n")

def salvaTxtNaoLancadas(codigo, dia):
	file = open("chamadas/naoLancadas.txt", 'a')
	file.write(str(codigo)+":"+str(dia) + "\n")

### INICIO

## DADOS DA PLANILHA
nomeDaPlanilha = "Copia de Presenca_DCC122_2016_3"
colunaMatriculas = 2 
colunaCodigos = 37

try:
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	sheet = client.open(nomeDaPlanilha).sheet1

except (httplib2.ServerNotFoundError):
	print ("Sistema offline")
	offline = True

operacao = raw_input("Insira a operacao a ser efetuada: \nCADASTRAR ONLINE = 1 \nCADASTRAR OFFLINE = 2 \nPRESENCA ONLINE = 3 \nPRESENCA OFFLINE = 4:\n")
if operacao == "1":
	cadastraCodigo(colunaMatriculas, colunaCodigos)
elif operacao == "2":
	cadastraOffline()
elif operacao == "3":
	lancaPresenca()
elif operacao == "4":
	lancaPresencaOffline()
else: 
	print "Opcao invalida."

	
