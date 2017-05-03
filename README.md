# acr122u-frequencia

## Leitura a partir de um PN532 no Orange Pi
### Utiliza as bibliotecas em C WiringOP (adaptação da WiringPi) para controle de I/O e Libnfc para controle do leitor NFC.
O programa em Python executa o código em C que efetua a leitura e retorna o valor pra uma variável no código em Python.
Maiores descrições sobre o projeto no Master Branch.

## Instruções ##

Documento editado neste exemplo:

https://docs.google.com/spreadsheets/d/1zS383tcuZqP1TerYZ5xqgfT9dS71JjeLaZ-Df8jzbvE/

### Instalar a WiringOP:

https://github.com/zhaolei/WiringOP

### Ativar as portas:
https://docs.armbian.com/harware_allwinner
ativar a uart3
Tomar cuidado ao usar o fex2bin (descrito no link acima) para salvar o setup.bin no local correto.
Para verificar quais são as portas no orange com suas correspondências para a WiringOP, basta digitar no terminal: 

```gpio readall```


### Instalar a libnfc1.7.1:
http://www.jamesrobertson.eu/blog/2016/feb/08/using-a-pn532-nfc-rfid-reader-with-the-raspberry-pi.html
Para testar o leitor, basta ir ao terminal e digitar:

 ``` sudo nfc-poll ```
    
   
O exemplo em questão faz a leitura de um único cartão e imprime as informações sobre ele. 


### Compilando o código em C:
```gcc -o leCartao lePython.c -lnfc -lwiringPi -lwiringPiDev -lpthread -lm```

