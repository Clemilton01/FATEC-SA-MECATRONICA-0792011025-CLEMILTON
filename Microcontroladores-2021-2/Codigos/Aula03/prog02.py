from machine import Pin
import time

#configura o LED Build in como saída
p2 = Pin(2, Pin.OUT)

#coloca o pino em nível alto
p2.on()

#Para o microcontrolador por 1 segundo
time.sleep(1)

#Pede para o microcontrolador desligar a saída
p2.off()