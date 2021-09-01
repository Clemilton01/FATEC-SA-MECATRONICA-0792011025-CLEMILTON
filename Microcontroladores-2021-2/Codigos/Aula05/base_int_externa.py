#Exemplo-INterrupcao
from machine import Pin
from time import sleep

#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

#Variável global
contador = 0

#Funcao que vai ser executada quando a interrupcao acontecer
def minha_funcao(fonte):
    global contador
    contador += 1
    print(contador,'- Aconteceu dentro da função!!')

#Configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)

#Configura a interrupção
bot1.irq(minha_funcao, trigger=Pin.IRQ_FALLING)

#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        pass
except:
    pass






