import serial
from pynput.keyboard import Key, Controller

COMPort = input('Enter COM port number: ')

try:
    scn = serial.Serial('COM' + COMPort, 9600)
except:
    print('No device detected in this COM port!')

keyboard = Controller()


def serialRead():
    try:
        scn.flushInput()

        incomingByte = scn.read()
        decodedByte = incomingByte.decode('utf-8')

        return decodedByte

    except:
        print('Communication error...or something')


def sendKeystroke():
    keyToSend = serialRead()

    if keyToSend != '':
        keyboard.tap(keyToSend)


while(True):
    sendKeystroke()



