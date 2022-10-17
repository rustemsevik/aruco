from machine import Pin
from time import sleep

'''**********************************

IN1 -->  16
IN2 -->  5
IN3 -->  4
IN4 -->  0
'''

in1 = Pin(16, Pin.OUT)
in2 = Pin(5, Pin.OUT)
in3 = Pin(4, Pin.OUT)
in4 = Pin(0, Pin.OUT)

in1.off()
in2.off()
in3.off()
in4.off()


   
for step in range(10000):
   
   
   #step1

    in1.on()
    in2.off()
    in3.off()
    in4.on()
    sleep(0.003)

    #step2

    in1.on()
    in2.on()
    in3.off()
    in4.off()
    sleep(0.003)

    #step3

    in1.off()
    in2.on()
    in3.on()
    in4.off()
    sleep(0.003)

    #step4

    in1.off()
    in2.off()
    in3.on()
    in4.on()
    sleep(0.003)

