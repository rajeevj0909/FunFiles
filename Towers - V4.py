def towers(disks):
    src = []
    aux = []
    dest = []
    for disk in range(disks):
        count=disks-disk
        src.insert(0,count)
    check=[]
    for n in src:
        check.append(n)
    print(src," ",aux," ",dest)
    reciept=[0]
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
        for move in range(2**disks-5):
            print(src," ",aux," ",dest)
            #print(reciept)
            if ((len(dest)==0)or(len(src)==0)or (dest[0]>src[0]))and ((len(dest)==0)or(len(src)==0) or((src[0])%2!=(dest[0])%2))and (len(src)!=0)and(reciept[0]!="t3-1"):
                reciept.insert(0,"t1-3")
                top=src[0]
                dest.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or(len(src)==0)or (aux[0]>src[0]))and ((len(aux)==0)or(len(src)==0) or((src[0])%2!=(aux[0])%2))and (len(src)!=0)and(reciept[0]!="t2-1"):
                reciept.insert(0,"t1-2")
                top=src[0]
                aux.insert(0,top)
                src.pop(0)
            elif ((len(aux)==0)or(len(dest)==0)or (aux[0]>dest[0]))and ((len(aux)==0)or(len(dest)==0) or((dest[0])%2!=(aux[0])%2))and (len(dest)!=0)and(reciept[0]!="t2-3"):
                reciept.insert(0,"t3-2")
                top=dest[0]
                aux.insert(0,top)
                dest.pop(0)
            elif ((len(src)==0)or(len(dest)==0)or (src[0]>dest[0]))and ((len(src)==0)or(len(dest)==0) or((dest[0])%2!=(src[0])%2))and (len(dest)!=0)and(reciept[0]!="t1-3"):
                reciept.insert(0,"t3-1")
                top=dest[0]
                src.insert(0,top)
                dest.pop(0)
            elif ((len(dest)==0)or(len(aux)==0)or (dest[0]>aux[0]))and ((len(dest)==0)or(len(aux)==0) or((aux[0])%2!=(dest[0])%2))and (len(aux)!=0)and(reciept[0]!="t3-2"):
                reciept.insert(0,"t2-3")
                top=aux[0]
                dest.insert(0,top)
                aux.pop(0)
            elif ((len(src)==0)or(len(aux)==0)or (src[0]>aux[0]))and ((len(src)==0)or(len(aux)==0) or((aux[0])%2!=(src[0])%2))and (len(aux)!=0)and(reciept[0]!="t1-2"):
                reciept.insert(0,"t2-1")
                top=aux[0]
                src.insert(0,top)
                aux.pop(0)
        
    print(src," ",aux," ",dest)
    if check==aux or check==dest:
        print("YOU BEAUTIFUL GENIUS!!!!!!!!!!!!!")
disks=4
towers(disks)

