# acr122u-frequencia
## Instruções ##

Documento editado neste exemplo:

https://docs.google.com/spreadsheets/d/1zS383tcuZqP1TerYZ5xqgfT9dS71JjeLaZ-Df8jzbvE/

1. Instale o python 2.7 ou superior:

https://www.python.org/downloads/release/python-2713/

2. Instale Swig:

windows: 

http://www.swig.org/download.html e defina path variable
Instale Visual c++ compiler pra python: 
https://www.microsoft.com/en-us/download/details.aspx?id=44266

linux:

sudo apt-get install swig

3. Instale as bibliotecas pyscard, httplib2, oauth2client e gspread:
  ``` 
  pip install pyscard gspread httplib2 oauth2client
  ```
  Caso não tenha pip:
  
  https://packaging.python.org/installing/
  
4. Para editar outra planilha, siga esses passos iniciais para configurar a google api (tem um gif):
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

OBS: ainda não implementei aceitação de utf-8, então planilhas com acentos ou ç não vão poder ser acessadas por enquanto

