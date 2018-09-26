import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
print ("Starting program")
GPIO.setup(22,GPIO.OUT)
# ser = serial.Serial('/dev/ttyS0', baudrate=9600,
#                     parity=serial.PARITY_NONE,
#                     stopbits=serial.STOPBITS_ONE,
#                     bytesize=serial.EIGHTBITS
#                     )
print ("started")
lastDrop=0
while True:
    #try:
    print "Dropping"
    lastDrop=int(round(time.time()*1000))


    GPIO.output(22,1)
    while True:
        now = int(round(time.time() * 1000))
        if (now-lastDrop)>=50:
            GPIO.output(22,0)
            break

    print "Waiting for stabilization"
    time.sleep(1)

    # try:
    #     print('Data Echo Mode Enabled')
    #
    #     print "reading... ",i
    #     if ser.inWaiting() > 0:
    #         data = ser.read()
    #         print "Data: ",data
    #         print "Data Length: ", len(data)
    #


    #except KeyboardInterrupt:
        #print("Exiting Program")

    #except:
        #print("Error Occurs, Exiting Program")

    #finally:
        #ser.close()
        #pass

