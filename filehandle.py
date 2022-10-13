import csv
from datetime import datetime


now = datetime.now()
cuurent_time = now.strftime("%H:%M:%S")
curentdate = now.strftime("%d/%m/%Y")

f = open(curentdate+'.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    lnwriter.writerow([now])
    f.close()
