import time
import serial

print ("Starting program")

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    print('Listening...')
    while True:
        data = ser.read()

        print(data)



finally:
    ser.close()
    pass

