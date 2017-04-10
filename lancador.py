import gspread
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

try:
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	sheet = client.open("Copia de Presenca_DCC122_2016_3").sheet1
except (httplib2.ServerNotFoundError):
	print ("Sistema offline")