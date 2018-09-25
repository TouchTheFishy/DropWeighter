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
        if ser.inWaiting() > 0:
            data = ser.read()
            if data.length > 0:
                print(data)

except KeyboardInterrupt:
    print ("Exiting Program")

except:
    print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass

