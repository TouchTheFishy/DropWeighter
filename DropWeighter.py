import time
import serial
import RPi.GPIO as GPIO
import xlwt as xw

GPIO.setmode(GPIO.BOARD)
print ("Starting program")

#Pin sur laquelle est branche le relais
ArduinoPin = 40

#sauvegarde de l'heure pour le nom du fichier log
now=time.strftime("%d%b_%H%M%S",time.localtime())
fileName="tests/"+now+".xls"

#creation du tableur de log
book=xw.Workbook()
sheet=book.add_sheet(str(now))
#insertion des entetes
sheet.write(0,0,'Drop')
sheet.write(0,1,'Weight (g)')

#mise de la pin du relai en sortie
GPIO.setup(ArduinoPin,GPIO.OUT)

#ouverture de la communication avec la balance
ser = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
print ("started")
lastDrop=0
lastWeight=0
i=1
while True:
    print "Dropping"
    #prise de l'heure a laquelle on a lache une goutte
    lastDrop=int(round(time.time()*1000))
    #activation du relais
    GPIO.output(ArduinoPin,0)
    while True:
        #on soustrait l'heure de "lachage" a l'heure actuelle
        now = int(round(time.time() * 1000))
        #on regarde si 50ms sont passees
        if (now-lastDrop)>=50:
            #si oui, on coupe le relais
            GPIO.output(ArduinoPin,1)
            break
    #on attend 3 secondes histoire que la balance se stabilise
    print "Waiting for stabilization"
    time.sleep(5)
    #vu que la balance envoie en continu, il faut vider le port avant de mesurer afin d'etre sur qu'on a la mesure
    #la plus recente
    ser.reset_input_buffer()
    time.sleep(0.5)

    try:


        print "Weighting... "
        if ser.inWaiting() > 0:
            #on lit les donnees du port
            data = ser.readline(16)
            while len(data)!=16:
                #on verifie que le message est bien complet (16 bytes)
                ser.reset_input_buffer()
                time.sleep(0.5)
                data = ser.readline(16)

            #on traduit les donnees recues en un truc lisible et on prend la valeur du
            parsed=data.split(" ")
            sheet.write(i, 0, i)
            dropWeight=float(parsed[5])-lastWeight
            lastWeight=float(parsed[5])
            sheet.write(i, 1, dropWeight)
            book.save(fileName)
            i += 1

            print("Drop Weight: "+str(dropWeight)+"g")
            print("")
            print("")




    except KeyboardInterrupt:
        ser.close()
        print("Exiting Program")


    finally:

        pass


