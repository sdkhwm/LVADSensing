import serial
import time
# Open the serial port
COMPort = 'COM11'
ser = serial.Serial(
    COMPort, 9600,
    timeout=0.02
    )  


ser.write('g r0x90\n'.encode())
baud = ser.readline().decode('utf-8')[2:]

print('Baud Rate is:')
print(baud)

#Change the Baud Rate to 115200
'''
if baud == '9600':
    ser.write('s r0x90 115200\n'.encode())
    time.sleep(1)
    print('baud rate changed to 115200')
'''

ser.write('s r0x90 115200\n'.encode())
time.sleep(1)
print('baud rate changed to 115200')

ser.close()

print('serial closed')