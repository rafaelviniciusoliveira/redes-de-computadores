from pyModbusTCP.client import ModbusClient
from random import randint
import time

# TCP auto connect on first modbus request
c = ModbusClient(host="localhost", port=502, auto_open=True)

# TCP auto connect on modbus request, close after it
c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)

c = ModbusClient()
c.host("localhost")
c.port(502)
# managing TCP sessions with call to c.open()/c.close()
c.open()

#variaveis de estado
alarme = 1
fan = 2
botaold = 3
valvula = 4


while True:
    #Botão de ligar e desligar o sistema (inicialmente desligado)
    botao = c.read_holding_registers(botaold)

    #sensor de temperatura
    temperatura = randint(0,40)

    #caso a temperatura esteja acima do limite:
    #limite = 1 (O fan será ativado)
    if temperatura > 20:
        limite = 1
        c.write_single_register(alarme,1)
    else:
        limite = 0
        c.write_single_register(alarme,0)

    print("temperatura: " ,temperatura)
    print("Limite: " ,limite)

    #Se o sistema estiver ligado e a temperatura atingiu o limite:
    #O fan será ligado e o alarme será ativado
    if botao == [1]:
        print("Sistema ligado")
        if limite != 0:
            if temperatura < 25:
                c.write_single_register(fan,3)

            if (temperatura >= 25) & (temperatura <=33):
                c.write_single_register(fan,6)

            if (temperatura > 33) & (temperatura <=40):
                c.write_single_register(fan,10)

            c.write_single_register(valvula,1)
        else:
            c.write_single_register(fan,0)
            c.write_single_register(valvula,0)
    else:
        c.write_single_register(fan,0)
        c.write_single_register(valvula,0)
        print("Sistema desligado")

    c.write_single_register(fan,5)

    time.sleep(7)
        
