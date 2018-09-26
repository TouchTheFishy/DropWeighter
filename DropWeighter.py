import time
import serial
import RPi.GPIO as GPIO
import xlwt as xw
GPIO.setmode(GPIO.BOARD)
print ("Starting program")

ArduinoPin = 22

now=time.strftime("%d%b_%H%M",time.localtime())
fileName=now+".xls"
book=xw.Workbook()
sheet=book.add_sheet(str(now))
sheet.write(0,0,'Iteration')
sheet.write(0,1,'Weight')
GPIO.setup(ArduinoPin,GPIO.OUT)
ser = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
print ("started")
lastDrop=0
lastweight=0
i=1
while True:
    print "Dropping"
    lastDrop=int(round(time.time()*1000))
    GPIO.output(22,1)
    while True:
        now = int(round(time.time() * 1000))
        if (now-lastDrop)>=50:
            GPIO.output(22,0)
            break

    print "Waiting for stabilization"
    time.sleep(3)
    ser.reset_input_buffer()
    time.sleep(0.5)

    try:
        print('Data Echo Mode Enabled')

        print "Weighting... "
        if ser.inWaiting() > 0:
            data = ser.readline(16)
            while len(data)!=16:
                ser.reset_input_buffer()
                time.sleep(0.5)
                data = ser.readline(16)
            parsed=data.split(" ")
            sheet.write(i, 0, i)
            dropWeight=float(parsed[5])-lastweight
            lastweight=float(parsed[5])
            sheet.write(i, 1, dropWeight)
            book.save(fileName)
            i += 1

            #print "Data: ",parsed[5]
            #print "Data Length: ", len(data)




    except KeyboardInterrupt:
        ser.close()
        print("Exiting Program")


    finally:

        pass


