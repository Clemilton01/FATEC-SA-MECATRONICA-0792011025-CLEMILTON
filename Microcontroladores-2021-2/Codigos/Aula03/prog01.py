from machine import Pin

#configura o LED Build in como saída
p2 = Pin(2, Pin.OUT)

#coloca o pino em nível alto
p2.on()