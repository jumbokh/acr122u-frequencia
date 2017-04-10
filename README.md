# acr122u-frequencia

#### frequencia.py:
Este script utiliza um leitor NFC para registrar o código do cartão de um aluno e sua presença em uma aula e lançar ambos em uma planilha do google. Ele também registra a presença e o cadastro de alunos no sistema em arquivos .txt fácilmente exportáveis para a planilha.

#### lancador.py:
Lança na planilha os cadastros e presenças armazenados offline.


## Instruções ##

Documento editado neste exemplo:

https://docs.google.com/spreadsheets/d/1zS383tcuZqP1TerYZ5xqgfT9dS71JjeLaZ-Df8jzbvE/

### 1. Instale os drivers do leitor:

http://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/

### 2. Instale o python 2.7 ou superior:

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

### 3. Instale Swig:

#### windows: 

http://www.swig.org/download.html e defina path variable

(mesma lógica do caso acima, é só colocar o diretório dele no lugar do diretório do python)

##### Instale Visual c++ compiler pra python: 

https://www.microsoft.com/en-us/download/details.aspx?id=44266

#### linux:
```
sudo apt-get install swig
```

### 4. Instale as bibliotecas pyscard, httplib2, oauth2client e gspread:
  ```  
  pip install pyscard gspread httplib2 oauth2client
  ```
  Caso não tenha pip:
  
  https://packaging.python.org/installing/
  
  Caso use Windows, defina a path variable com:

```
$env:path="$env:Path;C:\Python27\Scripts"
```
### 5. Execute o arquivo navegando pelo terminal ou prompt de comando até a pasta em que ele se encontra e digitando:

  ```
  python frequencia.py
  ```
  
### 6. Para editar outra planilha, siga esses passos iniciais para configurar a google api (siga os passos até o segundo gif):
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

Substitua o client_secret.json presente na pasta pelo seu, obtido seguindo os passos do tutorial acima.

Em seguida, modifique nos arquivos frequencia.py e lancador.py as variáveis:

```
nomedaPlanilha
colunaMatriculas
colunaCodigos
```

### OBS 1: 
Para finalizar o programa, pressione Ctrl + C

### OBS 2:
ainda não implementei aceitação de utf-8, então planilhas que tenham acentos ou ç no título não vão poder ser acessadas por enquanto.

### OBS 3:
no caso do seu linux ser de uma distro não debian-based, substitua apt-get por seu gerenciador de pacotes correspondente.

### Próximas atualizações previstas:

 -Colocar 0 para todos os alunos na coluna do dia em questão antes de iniciar a chamada do dia;
 
 -Apagar o naoLancadas.txt após o lançamento na planilha;
 
 -Opção para chamar o método de cadastrar o cartão em questão quando tentar responder chamada e não estiver registrado;
 
 -Implementar um setup.py pra definir os dados da planilha para edição;
 
 -Otimizações em geral.
 
