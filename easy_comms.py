#Easy comms is a simple class that allows you to send and receive messages over a serial port.

from machine import UART, Pin

class Easy_comms:
 
    uart_id = 0
    baud_rate = 9600
    
    def __init__(self, uart_id:int, baud_rate:int=None):
        self.uart_id = uart_id
        if baud_rate: self.baud_rate = baud_rate

        # set the baud rate
        self.uart = UART(self.uart_id,self.baud_rate)

        # Initialise the UART serial port
        self.uart.init()
            
    def send(self, message):
        print(f'sending message: {message}')
        self.uart.write(bytes(message,'utf-8'))
        
    def start(self):
        message = "ahoy\n"
        print(message)
        self.send(message)

    def read(self)->str:
        if self.uart.any() > 0: 
            return self.uart.readline().decode('utf-8')
        else:
            return None
        