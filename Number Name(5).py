units = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']

decimal=0
number=str(input("Whats your number?"))
str_lst=[]
element=0
for digit in number:
  str_lst.append(number[element])
  element=element+1

if (str_lst[0])=="-":
  str_lst.pop(0)
  print("Minus ",end="")
  
counter=0
length=len (str_lst)
for i in str_lst:
  if i==".":
    decimal=1
    str_lst.pop(counter)
    decimals=[]
    for dcml in range (counter,len (str_lst),1):
      decimals.append(str_lst[counter])
      str_lst.pop(counter)
    dec_int=[]
    dec_int = [int(element) for element in decimals]
  counter=counter+1


def normal(str_lst):
  int_lst=[]
  int_lst = [int(element) for element in str_lst]
  if len(int_lst)==1:
    position=int_lst[0]
    print(units[position],end="")
  elif len(int_lst)==2:
    if int_lst[0]==1:
      position=int_lst[1]
      print(teens[position],end="")
    else:
      unit=int_lst[1]
      ten=int_lst[0]        
      print(tens[ten]+" "+units[unit],end="")
  elif len(int_lst)==3:
    if number=="100":
      print ("A Hundred",end="")
    elif int_lst[1]==1:
      teen=int_lst[2]
      hundred=int_lst[0]
      print(units[hundred]+" Hundred and "+teens[teen],end="")
    else:
      unit=int_lst[2]
      ten=int_lst[1]
      hundred=int_lst[0]
      print(units[hundred]+" Hundred and "+tens[ten]+" "+units[unit],end="")
  elif len(int_lst)==4:
    if number=="1000":
      print ("A Thousand",end="")
    elif int_lst[2]==1:
      teen=int_lst[3]
      hundred=int_lst[1]
      thousand=int_lst[0]
      print(units[thousand]+" Thousand "+units[hundred]+" Hundred and "+teens[teen],end="")
    else:
      unit=int_lst[3]
      ten=int_lst[2]
      hundred=int_lst[1]
      thousand=int_lst[0]
      print(units[thousand]+" Thousand "+units[hundred]+" Hundred and "+tens[ten]+" "+units[unit],end="")
    
normal(str_lst)
if decimal==1:
  count=0
  print(" Point ",end="")
  for digit in dec_int:
    position=dec_int[count]
    print(units[position],end=" ")
    count=count+1


