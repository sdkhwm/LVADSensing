import numpy as np
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import serial
import pandas as pd
import msvcrt

#Functions###########################################################################################

def SerialReadVelocity():
    ser.write('g r0x18\n'.encode())
    #speed = ser.readline().decode('utf-8')[2:]
    speed = ser.read_until(b'\r').decode('utf-8').strip()[2:]
    return float(speed)/10

def SerialReadCurrent():
    ser.write('g r0x0c\n'.encode())
    #current = ser.readline().decode('utf-8')[2:]
    current = ser.read_until(b'\r').decode('utf-8').strip()[2:]
    return float(current)

###################################################################################################
Ts = []
Vs = []
Is = []


# Open the serial port
COMPort = 'COM11'
ser = serial.Serial(
    COMPort, 115200,
    timeout=0.1
    )  

print('serial port opened')


# Write data to the serial port

timestart = time.time()

while True:
    VelData = SerialReadVelocity()
    CurrentData = SerialReadCurrent()
    Ts.append(time.time()-timestart)
    Vs.append(VelData)
    Is.append(CurrentData)
        
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\r':
            break
        


#Format the Data into a dataframe
data = {
    "Condition": "MHF"
    "Time":Ts,
    "RPM":Vs,
    "Current":Is
    }

df = pd.DataFrame(data)

#Save the data to csv
df.to_csv('2025_01_08_Healthy80BPM.csv')
print("File Saved")

ser.close()
print('Serial Port Closed')