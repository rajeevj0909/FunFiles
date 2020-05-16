def towers(disks,src,aux,dest,counter,reciept,check):
    counter=counter+1
    s=(len(src))-1
    a=(len(aux))-1
    d=(len(dest))-1
    src.pop(s)
    aux.pop(a)
    dest.pop(d)
    print(src," ",aux," ",dest)
    src.insert(s,99)
    aux.insert(a,88)
    dest.insert(d,99)
    def move(change,come,go):
        reciept.insert(0,change)
        top=come.pop(0)
        go.insert(0,top)
    if check==dest:
        print(str(counter+1)+" Moves   " +str(disks)+" Disks")
        return("DONE!!!!")
    elif ((len(dest)==0)or (dest[0]>src[0]))and ((src[0])%2!=(dest[0])%2)and (len(src)>0)and(reciept[0]!="t3-1"):
        move("t1-3",src,dest)
    elif ((len(aux)==0)or (aux[0]>src[0]))and ((src[0])%2!=(aux[0])%2)and (len(src)>0)and(reciept[0]!="t2-1"):
        move("t1-2",src,aux)
    elif ((len(aux)==0)or (aux[0]>dest[0]))and ((dest[0])%2!=(aux[0])%2)and (len(dest)>0)and(reciept[0]!="t2-3"):
        move("t3-2",dest,aux)
    elif ((len(src)==0)or (src[0]>dest[0]))and ((dest[0])%2!=(src[0])%2)and (len(dest)>0)and(reciept[0]!="t1-3"):
        move("t3-1",dest,src)
    elif ((len(dest)==0)or (dest[0]>aux[0]))and ((aux[0])%2!=(dest[0])%2)and (len(aux)>0)and(reciept[0]!="t3-2"):
        move("t2-3",aux,dest)
    elif ((len(src)==0)or (src[0]>aux[0]))and ((aux[0])%2!=(src[0])%2)and (len(aux)>0)and(reciept[0]!="t1-2"):
        move("t2-1",aux,src)
    towers(disks,src,aux,dest,counter,reciept,check)
    
disks=int(input("How many disks? Make it an even number pls!"))
#Lists
src = [99]
aux = [88]
dest = [99]
#Create src
for disk in range(disks):
    count=disks-disk
    src.insert(0,count)
#Create checker
check=[]
for n in src:
    check.append(n)
#Print list
s=(len(src))-1
a=(len(aux))-1
d=(len(dest))-1
src.pop(s)
aux.pop(a)
dest.pop(d)
print(src," ",aux," ",dest)
src.insert(s,99)
aux.insert(a,88)
dest.insert(d,99)
#DONE
reciept=[0]
counter=0
even=False
##START OF GAME
if disks%2==1:
    top=src[0]
    dest.insert(0,top)
    src.pop(0)
    reciept.insert(0,"t1-3")
else:
    top=src[0]
    aux.insert(0,top)
    src.pop(0)
    reciept.insert(0,"t1-2")
    even=True
towers(disks,src,aux,dest,counter,reciept,check)





