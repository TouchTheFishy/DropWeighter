import time
import xlwt as xw

now=time.strftime("%d%b_%H%M",time.localtime())
fileName=now+".xls"
book=xw.Workbook()
sheet=book.add_sheet(str(now))
sheet.write(0,0,'Iteration')
sheet.write(0,1,'Weight')

i=1
while True:
    data="lol"
    sheet.write(i,0,i)
    sheet.write(i,1,data)
    book.save(fileName)
    i+=1
    time.sleep(1)