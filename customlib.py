from machine import Pin
from time import sleep

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

in1 = Pin(16, Pin.OUT)
in2 = Pin(5, Pin.OUT)
in3 = Pin(4, Pin.OUT)
in4 = Pin(0, Pin.OUT)

in1_2 = Pin(10, Pin.OUT)
in2_2 = Pin(9, Pin.OUT)
in3_2 = Pin(14, Pin.OUT)
in4_2 = Pin(12, Pin.OUT)

in1.off()
in2.off()
in3.off()
in4.off()

in1_2.off()
in2_2.off()
in3_2.off()
in4_2.off()

def left(aaa):
    for step in range(aaa):
       
       #step1
        in1.on()
        in1_2.on()
        in2.off()
        in2_2.off()
        in3.off()
        in3_2.off()
        in4.on()
        in4_2.on()
        sleep(0.003)

        #step2
        in1.on()
        in1_2.on()
        in2.on()
        in2_2.on()
        in3.off()
        in3_2.off()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step3
        in1.off()
        in1_2.off()
        in2.on()
        in2_2.on()
        in3.on()
        in3_2.on()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step4
        in1.off()
        in1_2.off()
        in2.off()
        in2_2.off()
        in3.on()
        in3_2.on()
        in4.on()
        in4_2.on()
        sleep(0.003)

    in1.off()
    in2.off()
    in3.off()
    in4.off()
    in1_2.off()
    in2_2.off()
    in3_2.off()
    in4_2.off()

def right(aaa):
    for step in range(aaa):
       
       #step1
        in1.off()
        in1_2.off()
        in2.off()
        in2_2.off()
        in3.on()
        in3_2.on()
        in4.on()
        in4_2.on()
        sleep(0.003)

        #step2
        in1.off()
        in1_2.off()
        in2.on()
        in2_2.on()
        in3.on()
        in3_2.on()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step3
        in1.on()
        in1_2.on()
        in2.on()
        in2_2.on()
        in3.off()
        in3_2.off()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step4
        in1.on()
        in1_2.on()
        in2.off()
        in2_2.off()
        in3.off()
        in3_2.off()
        in4.on()
        in4_2.on()
        sleep(0.003)

    in1.off()
    in2.off()
    in3.off()
    in4.off()
    in1_2.off()
    in2_2.off()
    in3_2.off()
    in4_2.off()

def forward(steps):
    for step in range(steps):

        #step1
        in1.on()
        in1_2.on()
        in2.off()
        in2_2.off()
        in3.on()
        in3_2.off()
        in4.on()
        in4_2.on()
        sleep(0.003)

        #step2
        in1.off()
        in1_2.on()
        in2.on()
        in2_2.on()
        in3.on()
        in3_2.off()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step3
        in1.on()
        in1_2.off()
        in2.on()
        in2_2.on()
        in3.off()
        in3_2.on()
        in4.off()
        in4_2.off()
        sleep(0.003)

        #step4
        in1.on()
        in1_2.off()
        in2.off()
        in2_2.off()
        in3.off()
        in3_2.on()
        in4.on()
        in4_2.on()
        sleep(0.003)

    in1.off()
    in2.off()
    in3.off()
    in4.off()
    in1_2.off()
    in2_2.off()
    in3_2.off()
    in4_2.off()
