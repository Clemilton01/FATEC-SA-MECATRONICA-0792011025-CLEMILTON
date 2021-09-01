#Exemplo-INterrupcao
from machine import Pin, Timer
#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1
#Funções que serão executadas quando o timer acontecer
def funcao1(t):
    print('Ola eu sou a função 1', t)
def funcao2(t):
    print('ola eu sou a funcao 2', t)
#Configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)
#Configura a interrupção
timer0 = Timer(0)
timer1 = Timer(1)
timer0.init(period=5000, mode=Timer.ONE_SHOT, callback=funcao1)
timer1.init(period=10000, mode=Timer.PERIODIC, callback=funcao2)
#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        pass
except:
    timer0.deinit()
    timer1.deinit()