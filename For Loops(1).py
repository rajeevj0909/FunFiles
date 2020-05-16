lists=[10,20,30,40,50,60,70,80,90,40]
number=int(input("What u want bro?"))
counter=0
for item in lists:
    counter=counter+1
    if number==item:
        print(counter)
