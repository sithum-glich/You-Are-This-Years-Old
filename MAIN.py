#birthday cal by WECA_KOLLAH
import time
from datetime import date
import calfun
date= date.today()
y= date.year
m= date.month
d= date.day
print (y,m,d)
while True:
     by= int(input("enter bith year"))
     bm=int(input("enter bith month"))
     bd=int(input("enter bith day"))
     calfun.cal(y,m,d,by,bm,bd)
