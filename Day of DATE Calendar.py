#https://youtu.be/714LTMNJy5M
#https://drive.google.com/file/d/1z7yZrCbqlHpiQCpmww7ohdj4ODzbrxtY/view

def format_date(date):
   date=list(date)
   no_date=int(date[0])*10
   no_date=no_date+int(date[1])
   month=int(date[3])*10
   month=month+int(date[4])
   year=int(date[6])*1000
   year=year+(int(date[7])*100)
   year=year+(int(date[8])*10)   
   year=year+int(date[9])
   formatted_date=[no_date,month,year]
   return(formatted_date)

def day_calculator(date):
   days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
   doomsdays=[0,3,28,14,4,9,6,11,8,5,10,7,12]
   remaining=date[2] %100
   century=date[2]-remaining
   if century %400==0:
      century_code=2
   elif century %400==100:
      century_code=0
   elif century %400==200:
      century_code=5
   elif century %400==300:
      century_code=3
   a=century_code
   b=int(remaining/12)
   c=remaining%12
   d=int(c/4)
   e=a+b+c+d
   while e>5:
      e=e-7
   doomsday=doomsdays[date[1]]
   difference=date[0]-doomsday +e
   difference=difference%7
   return(days[difference])
      
date=input("What's the date? dd/mm/yyyy \n")   
int_date=format_date(date)
if int_date[0]<31 or int_date[0]>1 or int_date[1]<12 or int_date[1]>1 or int_date[2]<9999 or int_date[2]>0:
   print("This is a ",day_calculator(int_date),"!")
else:
   print("You entered a dodgy date!")
