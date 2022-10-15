import Stepper2
from machine import Pin

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
'''


motors = Stepper.create(Pin(16,Pin.OUT),Pin(5,Pin.OUT),Pin(4,Pin.OUT),Pin(0,Pin.OUT), Pin(10,Pin.OUT),Pin(9,Pin.OUT),Pin(14,Pin.OUT),Pin(12,Pin.OUT),delay = 2, mode='FULL_STEP')


double(1000,1)



