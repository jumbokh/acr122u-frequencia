import gspread
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

def lancaPresenca(colunaMatriculas): 

	a = 0
	numLinha = 1
	with open("chamadas/naoLancadas.txt", 'r') as file:
		for line in file:
			line = line.strip()
			linhaAtual = line.split(":")
			dia = linhaAtual[1]
			codigo = linhaAtual[0]
			with open("chamadas/presencas lancadas/"+dia+".txt", 'a') as file2:
				print "Buscando codigo " + str(numLinha) + " na planilha"
				try:
					coluna = sheet.find(dia).col
					linha = sheet.find(codigo).row
				except (gspread.exceptions.CellNotFound):
					print "Codigo ou dia invalido"
				except (NameError):
					print "Sistema Offline"
				else:
					sheet.update_cell(linha, coluna, 1)
					print "Presenca lancada na planilha"
					file2.write(str(codigo)+ "\n")
					print "Presenca lancado no txt\n"
				numLinha += 1



def lancaCadastro(colunaMatriculas, colunaCodigos):
	a = 0

	numLinha = 1
	with open("cadastrar/cadastro.txt", 'r') as file, open("chamadas/naoLancadas.txt", 'a') as file2:
		for line in file:
			naoEncontrada = False
			line = line.strip() #tira o \n
			linhaAtual = line.split(":")
			matricula = linhaAtual[0]
			dia = linhaAtual[2]
			codigo = linhaAtual[1]
					
			try:
				a = sheet.find(matricula)
				if a.col != colunaMatriculas:
					print "Matricula " + str(numLinha) + " NAO encontrada"
					naoEncontrada = True
				else:
					print "Matricula " + str(numLinha) + " encontrada"
			except (gspread.exceptions.CellNotFound):
				print "Matricula " + str(numLinha) + " NAO encontrada"
				naoEncontrada = True
			except (NameError):
				print "Sistema offline."
			if (naoEncontrada == False):
				linha = a.row	
				sheet.update_cell(linha, colunaCodigos, codigo)
				print "Codigo " + str(numLinha) + " cadastrado"
				file2.write(codigo+":"+ dia + "\n")	
				print "Presenca " + str(numLinha) + " cadastrada em naoLancadas.txt"
			numLinha += 1
			print "\n"

## INCIO

## DADOS DA PLANILHA
nomedaPlanilha = "Copia de Presenca_DCC122_2016_3"
colunaMatriculas = 2
colunaCodigos = 37

try:
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	sheet = client.open(nomedaPlanilha).sheet1
except (httplib2.ServerNotFoundError):
	print ("Sistema offline")
	exit()

operacao = raw_input("Insira a operacao a ser efetuada (lancarPresenca = 1, lancarCadastro = 2):\n")
if operacao == "1":
	lancaPresenca(colunaMatriculas)
elif operacao == "2":
	lancaCadastro(colunaMatriculas, colunaCodigos)
else: 
	print "Opcao invalida."

