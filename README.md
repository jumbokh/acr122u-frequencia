# acr122u-frequencia
## Instruções ##

Documento editado neste exemplo:

https://docs.google.com/spreadsheets/d/1zS383tcuZqP1TerYZ5xqgfT9dS71JjeLaZ-Df8jzbvE/

### 1. Instale o python 2.7 ou superior:

#### windows:

https://www.python.org/downloads/release/python-2713/
 e defina path variable se necessário:

digite no prompt de comando: 

```
$env:path="$env:Path;C:\Python27"
```

#### linux:
```
sudo apt-get install python
```

### 2. Instale Swig:

#### windows: 

http://www.swig.org/download.html e defina path variable

(mesma lógica do caso acima, é só colocar o diretório dele no lugar do diretório do python)

Instale Visual c++ compiler pra python: 

https://www.microsoft.com/en-us/download/details.aspx?id=44266

#### linux:
```
sudo apt-get install swig
```

### 3. Instale as bibliotecas pyscard, httplib2, oauth2client e gspread:
  ```  
  pip install pyscard gspread httplib2 oauth2client
  ```
  Caso não tenha pip:
  
  https://packaging.python.org/installing/
  
  Caso use Windows, defina a path variable com:

```
$env:path="$env:Path;C:\Python27\Scripts"
```
  
### 4. Para editar outra planilha, siga esses passos iniciais para configurar a google api (tem um gif):
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

OBS: ainda não implementei aceitação de utf-8, então planilhas com acentos ou ç não vão poder ser acessadas por enquanto.

OBS: no caso do seu linux ser de uma distro não debian-based, substitua apt-get por seu gerenciador de pacotes correspondente.

