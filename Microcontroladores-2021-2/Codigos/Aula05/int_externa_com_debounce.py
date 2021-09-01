#Exemplo-INterrupcao
from machine import Pin
from time import sleep
import time

#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

#Variável global
contador = 0
tempo_bot1 = time.ticks_ms()
#Funcao que vai ser executada quando a interrupcao acontecer
def minha_funcao_up(fonte):
    global tempo_bot1
    if abs(time.ticks_diff(tempo_bot1, time.ticks_ms())) > 300:
        tempo_bot1 = time.ticks_ms()
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
bot1.irq(minha_funcao_up, trigger=Pin.IRQ_RISING)

#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        pass
except:
    pass







