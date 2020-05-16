
print("my names rajeev and im the worst coder i cant even code credit card validation. I will work at nandos forever because i love the discount.")
#Turns number into interger lists
number=input("What number?")
list1=list(number)
list2=[]
for n in list1:
  x=int(n)
  list2.append(x)
square=[]
total=11
#Runs function
def happy(list2,square,total):
  #If remainder is 1, its happy, it's also the base case
  if total==1:
    print(number+" is HAPPY!")
  #If remainder is between 1 and 10, its sad
  elif total<10:
    print(number+" is SAD!")
  #If the number is bigger than 10, it will shorten to 1 digit
  else:
    total=0
    print(list2)
    #Creates a list of squared digits
    for n in list2:
      sqrd=n**2
      square.append(sqrd)
    print(square)
    #Creates a total of the squared digits
    for n in square:
      total=total+n
    print(total)
    total=str(total)
    list1=list(total)
    list2=[]
    square=[]
    #Turns it into a integer list again
    for n in total:
      x=int(n)
      list2.append(x)
    total=int(total)
    #Recursion to make the total thats larger than 10 smaller
    happy(list2,square,total) 
    

#Runs the function
happy(list2,square,total)    
