units = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']


number=str(input("Whats your number bro?"))
str_lst=[]
element=0
for digit in number:
  str_lst.append(number[element])
  element=element+1

if (str_lst[0])=="-":
  str_lst.pop(0)
  print("Minus ",end="")


print(str_lst)#F
counter=0
length=len (str_lst)
for i in str_lst:
  if i==".":
    str_lst.pop(counter)
    print(str_lst)#F
    decimals=[]
    decimal_length=length-counter
    print (decimal_length)#F
    print(counter)#F
    for decimal_length in str_lst:
      decimals.append(str_lst[counter-1])
      str_lst.pop(counter-1)
    print(str_lst)#F
    print(decimals)#F
    dec_int=[]
    dec_int = [int(element) for element in decimals]
    count=0
    print(" Point ",end="")
    for digit in dec_int:
      position=dec_int[count]
      print(units[position]," ",end="")#F
      count=count+1
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
    else:
      unit=int_lst[2]
      ten=int_lst[1]
      hundred=int_lst[0]
      print(units[hundred]+" Hundred and "+tens[ten]+" "+units[unit],end="")
  elif len(int_lst)==4:
    if number=="1000":
      print ("A Thousand",end="")
    else:
      unit=int_lst[3]
      ten=int_lst[2]
      hundred=int_lst[1]
      thousand=int_lst[0]
      print(units[thousand]+" Thousand "+units[hundred]+" Hundred and "+tens[ten]+" "+units[unit],end="")
    
normal(str_lst)


