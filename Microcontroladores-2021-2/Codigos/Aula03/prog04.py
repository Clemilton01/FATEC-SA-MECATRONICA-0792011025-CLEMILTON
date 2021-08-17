import esp32
import time
from machine import RTC

#configurações globais
rtc = RTC()
rtc.datetime((2021, 8, 16, 2, 21, 20, 0, 0)) 
#converte de F para C
def converte_temperatura (tempF):
    return (tempF-32)*5/9

print("Monitoramento de Sensores:")
while True:
    #Ler sensores internos
    temperatura = esp32.raw_temperature()
    sensor_hall = esp32.hall_sensor()

    data_hora = rtc.datetime()

    #Exibe os valores dos sensores
    print('Temperatura:{} - {}'.format(converte_temperatura(temperatura),data_hora))
    print('Hall:{} - {}'.format(sensor_hall, data_hora))
    time.sleep(2)
