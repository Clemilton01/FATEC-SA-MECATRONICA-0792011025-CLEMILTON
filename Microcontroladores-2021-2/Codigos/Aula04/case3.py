#Case 3
from machine import Pin
from time import sleep
 
#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1
 
#Configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)
 
#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        #Lógica do botão 1
        if bot1.value() == BOTAO_ACIONADO:
            led1.value(LED_LIGADO)
        else:
            led1.value(LED_DESLIGADO)
        #Lógica do botão 2
        if bot2.value() == BOTAO_ACIONADO:
            led2.value(LED_LIGADO)
        else:
            led2.value(LED_DESLIGADO)
except:
    #Rotina que será executada quando o código tiver sua execução interrompida
    led1.value(LED_DESLIGADO)
    led2.value(LED_DESLIGADO)
 