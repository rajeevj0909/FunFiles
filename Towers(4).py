import time
def towers(disks):
    src = [99]
    aux = [88]
    dest = [99]
    for disk in range(disks):
        count=disks-disk
        src.insert(0,count)
    check=[]
    for n in src:
        check.append(n)
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
    reciept=[0]
    counter=0
    ##START OF GAME
    if disks%2==1:
        top=src[0]
        dest.insert(0,top)
        src.pop(0)
        reciept.insert(0,"t1-3")
        for move in range(2**disks-2):
            time.sleep(1)
            print(reciept)
            counter=counter+1
            s=(len(src))-1
            d=(len(dest))-1
            a=(len(aux))-1
            src.pop(s)
            dest.pop(d)
            aux.pop(a)
            print(src," ",aux," ",dest)
            src.insert(s,99)
            dest.insert(d,88)
            aux.insert(a,99)
            if ((len(dest)==0)or (dest[0]>src[0]))and ((src[0])%2!=(dest[0])%2)and (len(src)>0)and(reciept[0]!="t3-1"):
                reciept.insert(0,"t1-3")
                top=src[0]
                dest.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or (aux[0]>src[0]))and ((src[0])%2!=(aux[0])%2)and (len(src)>0)and(reciept[0]!="t2-1"):
                reciept.insert(0,"t1-2")
                top=src[0]
                aux.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or (aux[0]>dest[0]))and ((dest[0])%2!=(aux[0])%2)and (len(dest)>0)and(reciept[0]!="t2-3"):
                reciept.insert(0,"t3-2")
                top=dest[0]
                aux.insert(0,top)
                dest.pop(0)
            elif ((len(src)==0)or (src[0]>dest[0]))and ((dest[0])%2!=(src[0])%2)and (len(dest)>0)and(reciept[0]!="t1-3"):
                reciept.insert(0,"t3-1")
                top=dest[0]
                src.insert(0,top)
                dest.pop(0)
            elif ((len(dest)==0)or (dest[0]>aux[0]))and ((aux[0])%2!=(dest[0])%2)and (len(aux)>0)and(reciept[0]!="t3-2"):
                reciept.insert(0,"t2-3")
                top=aux[0]
                dest.insert(0,top)
                aux.pop(0)
            elif ((len(src)==0)or (src[0]>aux[0]))and ((aux[0])%2!=(src[0])%2)and (len(aux)>0)and(reciept[0]!="t1-2"):
                reciept.insert(0,"t2-1")
                top=aux[0]
                src.insert(0,top)
                aux.pop(0)
    else:
        top=src[0]
        aux.insert(0,top)
        src.pop(0)
        reciept.insert(0,"t1-2")
        for move in range(2**disks-2):
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
            if ((len(dest)==0)or (dest[0]>src[0]))and ((src[0])%2!=(dest[0])%2)and (len(src)>0)and(reciept[0]!="t3-1"):
                reciept.insert(0,"t1-3")
                top=src[0]
                dest.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or (aux[0]>src[0]))and ((src[0])%2!=(aux[0])%2)and (len(src)>0)and(reciept[0]!="t2-1"):
                reciept.insert(0,"t1-2")
                top=src[0]
                aux.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or (aux[0]>dest[0]))and ((dest[0])%2!=(aux[0])%2)and (len(dest)>0)and(reciept[0]!="t2-3"):
                reciept.insert(0,"t3-2")
                top=dest[0]
                aux.insert(0,top)
                dest.pop(0)
            elif ((len(src)==0)or (src[0]>dest[0]))and ((dest[0])%2!=(src[0])%2)and (len(dest)>0)and(reciept[0]!="t1-3"):
                reciept.insert(0,"t3-1")
                top=dest[0]
                src.insert(0,top)
                dest.pop(0)
            elif ((len(dest)==0)or (dest[0]>aux[0]))and ((aux[0])%2!=(dest[0])%2)and (len(aux)>0)and(reciept[0]!="t3-2"):
                reciept.insert(0,"t2-3")
                top=aux[0]
                dest.insert(0,top)
                aux.pop(0)
            elif ((len(src)==0)or (src[0]>aux[0]))and ((aux[0])%2!=(src[0])%2)and (len(aux)>0)and(reciept[0]!="t1-2"):
                reciept.insert(0,"t2-1")
                top=aux[0]
                src.insert(0,top)
                aux.pop(0)
    
    s=(len(src))-1
    a=(len(aux))-1
    d=(len(dest))-1
    src.pop(s)
    aux.pop(a)
    dest.pop(d)
    print(src," ",aux," ",dest)
    print(str(counter+2)+" Moves   " +str(disks)+" Disks")


disks=int(input("How many disks? Make it an even number pls!"))
towers(disks)



