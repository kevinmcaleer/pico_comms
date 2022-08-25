# led_client

from easy_comms import Easy_comms
from time import sleep
from machine import Pin
import json

com1 = Easy_comms(0,9600)
led = Pin("LED", Pin.OUT, value=0)

while True:
    message = com1.read()
    try:
        command = json.loads(message)
        if command is not None:
            if command['command'] == 'blink':
                if command['args'] == 'on':
                    led.on()
                if command['args'] == 'off':
                    led.off()
        sleep(0.01)
    except Exception as e:
        print(f'error: {e}')
