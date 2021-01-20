import RPi.GPIO as GPIO
import time
import socket
import threading


relay_pin = 23
sensor_pin = 14



HOST = '10.247.169.48'
PORT = 12351

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
    
#try to connect to port (check if port is available)
try:
    s.bind((HOST, PORT))
except socket.error:
    print('bind failed')
    
#get first message
s.listen(1)
print("Socket wait message")
(conn, addr) = s.accept()
print("connected")

def setup():
    print("Program starting")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.setup(sensor_pin, GPIO.IN)
    
    #initial lamp will be turned off
    GPIO.output(relay_pin, GPIO.LOW)
    
    #create socket for TCP connection
    
    
#basic functions
def turnOn():
    GPIO.output(relay_pin, GPIO.HIGH)
    conn.send("on".encode())

def turnOff():
    GPIO.output(relay_pin, GPIO.LOW)
    conn.send("off".encode())

def detechHuman():
    return GPIO.input(sensor_pin)==GPIO.HIGH

def timerTurnOn():
    ##("Enter the the time to turn on(after): ")
    ##duration = conn.recv(1024).decode()
    t = threading.Timer(5.0, turnOn)
    print("The lamp will turn on")
    t.start()
    
def timerTurnOff():      
    ##print("Enter the time to turn off(after): ")
    ##duration = conn.recv(1024).decode()
    t2 = threading.Timer(5.0, turnOff)
    print("The lamp will turn off")
    t2.start()
        
    
    
def loop():
    autoMode = False
    while True:
        data = conn.recv(1024).decode()
        
        
        #change autoMode if needed
        
        if (data == "auto mode off"):
            autoMode = False
            print("Auto-mode off")
            
        if (data == "auto mode on"):
            autoMode = True
            print("Auto-mode on")
            
        
        if (detechHuman() and autoMode == True):
            turnOn()
            print("Lamp is on")
        elif (autoMode == True):
            turnOff()
            print("Lamp is off")

        if (data == "turn on"):
            turnOn();
            print("Lamp is on")
        
        if (data == "turn off"):
            turnOff();
            print("Lamp is off")
            
            
        if (data == "timer light on"):
            timerTurnOn();
            print("Timer light on")
            
        if (data == "timer light off"):
            timerTurnOff();
            print("Timer light off")    
            
        if (data == "quit"):
            break
            
            
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Finished")
        GPIO.cleanup()