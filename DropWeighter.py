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
    time.sleep(10)
    ser.reset_input_buffer()
    time.sleep(0.5)

    try:
        print('Data Echo Mode Enabled')

        print "Weighting... "
        if ser.inWaiting() > 0:
            data = ser.readline(16)
            parsed=data.split(" ")

            print "Data: ",parsed
            print "Data Length: ", len(data)



    except KeyboardInterrupt:
        ser.close()
        print("Exiting Program")


    finally:

        pass


