#Insert card
card_number=[]
card=str(input("Whats your card number?"))
#Turns to integers
card_number=[int(i)for i in card]
#Drop last digit
print(card_number)
card1=card_number
card1.pop(len(card1)-1)
#Reverse digits
card2=[]
for n in card1:
    card2.insert(0,n)
card3=[]
#Multiple odd digits by 2:
for n in range(len(card2)):
    if n%2==0:
        x=card2[n]*2
        card3.append(x)
    else:
        card3.append(int(card2[n]))
#Subtract 9 to numbers over 9:
card4=[]
for n in card3:
    if n>9:
        card4.append(n-9)
    else:
        card4.append(n)
#Add all numbers
total=0
for n in card4:
    total=total+n

print(card1)
print(card2)
print(card3)
print(card4)
print(total)
#If mod 10 is last original digit, its valid
if total%10==card_number[len(card_number)-1]:
    print("VALID")
else:
    print("NOT VALID")

#4556737586899855
#This is valid
