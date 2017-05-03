#include <stdlib.h>
#include <nfc/nfc.h>
#include <wiringPi.h>
#include <time.h>
#include <math.h>

/*
led na porta 8 (é como o wiringPi reconhece a PA12,
para ver as correspondencias, digite no terminal:
gpio readall
*/
#define	LED	8 


// 062*10⁹+043*10⁶+219*10³+155*1
static unsigned long long int //le o id do cartão e converte pra unsigned long long int
read_int(const uint8_t *pbtData, const size_t szBytes)
{
  size_t  szPos;
  unsigned long long int idInt = 0;
	
  for (szPos = 0; szPos < szBytes; szPos++) {
	idInt += pbtData[szPos] * (pow(10,(szBytes - szPos - 1)*3));	
  }
  return idInt;
}

int main(int argc, const char *argv[])
{//iniciando wiringPi e definindo a porta como saida
  wiringPiSetup () ;
  pinMode (LED, OUTPUT) ;
  digitalWrite (LED, LOW) ;
    
  //definindo as variáveis e iniciando o libnfc
  nfc_device *pnd;
  nfc_target nt;
  nfc_context *context;
  nfc_init(&context);
  
  //detecção de erros, etc
  if (context == NULL) {
    printf("Unable to init libnfc (malloc)\n");
    exit(EXIT_FAILURE);
  }
  const char *acLibnfcVersion = nfc_version();
  (void)argc;
 
  pnd = nfc_open(context, NULL);

  if (pnd == NULL) {
    printf("ERROR: %s\n", "Unable to open NFC device.");
    exit(EXIT_FAILURE);
  }
  if (nfc_initiator_init(pnd) < 0) {
    nfc_perror(pnd, "nfc_initiator_init");
    exit(EXIT_FAILURE);
  }
  
  //reconhecendo o leitor e definindo o padrão mifare
  const nfc_modulation nmMifare = {
    .nmt = NMT_ISO14443A,
    .nbr = NBR_106,
  };
  
  //lendo o cartão e imprimindo o id
  if (nfc_initiator_select_passive_target(pnd, nmMifare, NULL, 0, &nt) > 0) { 
	digitalWrite (LED, HIGH) ;
	delay(500); //espera 0,5 segundo mantendo o led aceso
	printf("%llu",read_int(nt.nti.nai.abtUid, nt.nti.nai.szUidLen));
  }
  delay(500); //espera mais 0,5
  digitalWrite (LED, LOW) ;

  //finalizando a libnfc
  nfc_close(pnd);
  nfc_exit(context);
  exit(EXIT_SUCCESS);
}

