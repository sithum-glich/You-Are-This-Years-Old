def cal(y,m,d,by,bm,bd):
     ly = y-by
     if m>=bm:
          if (m==bm and d==bd):
               print( "happy bd you are" , ly , "years old")

          if (m==bm and d<bd):
               ly=ly-1
               lm = 11
               ld = d+30-bd
               print("you have lived for",ly, " years and",lm,"months and", ld," days")

          if(m>bm and bd==d):
               lm=m-bm
               print("you have lived for",ly, " years and",lm,"months")
          if(m>bm and d<bd):
               lm=m-bm-1
               ld=d+30-bd
               print("you have lived for",ly, " years and",lm,"months and", ld," days")
               
               
          if (m>bm and d>bd):
                lm=m-bm
                ld=d-bd
                print("you have lived for",ly, " years and",lm,"months and", ld," days")


     if(m<bm):

          if (d<bd):
               ly=ly-1
               lm=m+11-bm
               ld = d+30-bd
               print("you have lived for",ly, " years and",lm,"months and", ld," days")
          if(d>bd):
               ly=ly-1
               lm=m+12-bm
               ld= d-bd
               print("you have lived for",ly, " years and",lm,"months and", ld," days")

          if bd==d:
               ly=ly-1
               lm=m+12-bm
               print("you have lived for",ly, " years and",lm,"months ")
