import paho.mqtt.client as mqtt
import keyboard

# This is the Publisher

broker_addr = "192.168.0.201"
topic = "deneme"

client = mqtt.Client()
client.connect(broker_addr, 1883, 60)
client.publish(topic, "Hello esp32 Rustem connected")

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed
            client.publish(topic, "w")
            print('W: Forward')
        elif keyboard.is_pressed('s'):
            client.publish(topic, "s")
            print('S: Backward')
        elif keyboard.is_pressed('a'):
            client.publish(topic, "a")
            print('A: Left')
        elif keyboard.is_pressed('d'):
            client.publish(topic, "d")
            print('D: Right')

    except:
        break  # if user pressed a key other than the given key the loop will break


