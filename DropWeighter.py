import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
print ("Starting program")

ArduinoPin = 22

now=time.strftime("%d%b_%H%M",time.localtime())
fileName="Test_"+now+".txt"
f=open(fileName,'w')
f.write('Drop   Weight'+"\n")
f.close()
GPIO.setup(ArduinoPin,GPIO.OUT)
ser = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
print ("started")
lastDrop=0
i=0
while True:
    print "Dropping"
    lastDrop=int(round(time.time()*1000))
    GPIO.output(22,1)
    while True:
        now = int(round(time.time() * 1000))
        if (now-lastDrop)>=1000:
            GPIO.output(22,0)
            break

    print "Waiting for stabilization"
    time.sleep(5)

    try:
        print('Data Echo Mode Enabled')

        print "Weighting... "

        data = ser.read(16)
        print "Data: ",data
        print "Data Length: ", len(data)



    except KeyboardInterrupt:
        print("Exiting Program")


    finally:
        ser.close()
        pass


