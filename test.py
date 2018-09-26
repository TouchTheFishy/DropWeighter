import time
import xlwt

now=time.strftime("%d%b_%H%M",time.localtime())
fileName="Test_"+now+".xls"
f=open(fileName,'w')
f.write('Drop   Weight'+"\n")
f.close()
i=0
while True:
    data="lol"
    f = open(fileName, 'a')
    string=str(i) + "    " + str(data) + "\n"
    f.write(string)
    f.close()
    i+=1
    time.sleep(5)