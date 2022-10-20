import network
from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import Stepper
import Stepper2


'''**********************************
# For right motor the pins are listed below
IN1 -->  14
IN2 -->  12
IN3 -->  13
IN4 -->  15
# For left motor the pins are listed below
IN1 -->  16
IN2 -->  5
IN3 -->  4
IN4 -->  0
'''**********************************

right_motor = Stepper.create(Pin(10,Pin.OUT),Pin(9,Pin.OUT),Pin(14,Pin.OUT),Pin(12,Pin.OUT), delay=2)
left_motor = Stepper.create(Pin(16,Pin.OUT),Pin(5,Pin.OUT),Pin(4,Pin.OUT),Pin(0,Pin.OUT), delay=2)


BROKER_ADDR = "192.168.0.196"
CLIENT_ID = "client"
TOPIC = "rot_commands"

print(1)
c = MQTTClient(CLIENT_ID ,BROKER_ADDR , keepalive = 60)
print(2)
c.connect()
print(3)
c.publish('Report_Channel', 'ESP initialized and client is connected to the broker')
print(4)

def message_printer(topic, msg):
    message = msg.decode()
    print(message)
    return message

c.set_callback(message_printer)
print(5)
c.subscribe(TOPIC)
print(6)
c.publish('Report_Channel', 'ESP client is subscribed to the topic rot_commands')
print(7)

while True:
    c.check_msg()
    if message == "Turn_Right":
        #Directions are not specified!!! 
        left_motor.angle(80,-1)
        sleep(0.25)
    elif message == "Turn_Left":
        right_motor.angle(10,-1)
        left_motor.angle(10,-1)
        sleep(0.25)
    elif message == "Move_Forward":
        right_motor.angle(10,-1)
        left_motor.angle(10,-1)
        sleep(0.25)
    



