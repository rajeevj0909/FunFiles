def towers(disks):
    src = [99,88]
    aux = [88,99]
    dest = [99,88]
    for disk in range(disks):
        count=disks-disk
        src.insert(0,count)
    check=[]
    for n in src:
        check.append(n)
    print(src," ",aux," ",dest)
    reciept=[0]
    def validation(tower1,tower2,move,reciept):
        if (tower1[0])%2==(tower2[0])%2 :
            print("Validation1")
            return("break")
        if (reciept[0]==move):
            print("Validation2")
            return("break")
    def skips():
        skip1=False
        skip1=False
        skip2=False
        skip3=False
        skip4=False
        skip5=False
        skip6=False
    skip1=False
    skip2=False
    skip3=False
    skip4=False
    skip5=False
    skip6=False 
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
        for move in range(2**disks-8):
            print("\n")
            print(src," ",aux," ",dest)
            print(reciept)
            if ((len(dest)==0)or (dest[0]>src[0]))and (len(src)>0)and(skip1==False):
                print("1 tooo 3")
                if validation(src,dest,"t3-1",reciept)=="break":
                    skip1=True
                else:
                    print("t1-3")
                    reciept.insert(0,"t1-3")
                    top=src[0]
                    dest.insert(0,top)
                    src.pop(0)
                    skips()
            elif ((len(aux)==0)or (aux[0]>src[0]))and (len(src)>0)and(skip2==False):
                print("1 tooo 2")
                if validation(src,aux,"t2-1",reciept)=="break":
                    skip2=True
                else:
                    print("t1-2")
                    reciept.insert(0,"t1-2")
                    top=src[0]
                    aux.insert(0,top)
                    src.pop(0)
                    skips()
            elif ((len(aux)==0)or (aux[0]>dest[0]))and (len(dest)>0)and(skip3==False):
                print("3 tooo 2")
                if validation(dest,aux,"t2-3",reciept)=="break":
                    skip3=True
                else:
                    print("t3-2")
                    reciept.insert(0,"t3-2")
                    top=dest[0]
                    aux.insert(0,top)
                    dest.pop(0)
                    skips()
            elif ((len(src)==0)or (src[0]>dest[0]))and (len(dest)>0)and(skip4==False):
                print("3 tooo 1")
                if validation(dest,src,"t1-3",reciept)=="break":
                    skip4=True
                else:
                    print("t3-1")
                    reciept.insert(0,"t3-1")
                    top=dest[0]
                    src.insert(0,top)
                    dest.pop(0)
                    skips()
            elif ((len(dest)==0)or (dest[0]>aux[0]))and (len(aux)>0)and(skip5==False):
                print("2 tooo 3")
                if validation(aux,dest,"t3-2",reciept)=="break":
                    skip5=True
                else:                    
                    print("t2-3")
                    reciept.insert(0,"t2-3")
                    top=aux[0]
                    dest.insert(0,top)
                    aux.pop(0)
                    skips()
                    skip5=False
            elif ((len(src)==0)or (src[0]>aux[0]))and (len(aux)>0)and(skip6==False):
                print("2 tooo 1")
                if validation(aux,src,"t1-2",reciept)=="break":
                    skip6=True
                else:
                    print("t2-1")
                    reciept.insert(0,"t2-1")
                    top=aux[0]
                    src.insert(0,top)
                    aux.pop(0)
                    skips()
            else:
                print("Run out of moves")
            
    
    
            
            


        '''for move in range(2**disks-1):
        if 5>6:
            print("IMPOSIBBLE")
        elif ((len(dest)==0)or (dest[0]>disk))and (len(src)>0):
            print("t1-3")
            top=src[0]
            dest.insert(0,top)
            src.pop(0)
        elif ((len(aux)==0)or (aux[0]>disk))and (len(src)>0):
            print("t1-2")
            top=src[0]
            aux.insert(0,top)
            src.pop(0)
        elif ((len(aux)==0)or (aux[0]>disk))and (len(dest)>0):
            print("t3-2")
            top=dest[0]
            aux.insert(0,top)
            dest.pop(0)
        elif ((len(src)==0)or (src[0]>disk))and (len(dest)>0):
            print("t3-1")
            top=dest[0]
            src.insert(0,top)
            dest.pop(0)
        elif ((len(dest)==0)or (dest[0]>disk))and (len(aux)>0):
            print("t2-3")
            top=aux[0]
            dest.insert(0,top)
            aux.pop(0)
        elif ((len(src)==0)or (src[0]>disk))and (len(aux)>0):
            print("t2-1")
            top=aux[0]
            src.insert(0,top)
            aux.pop(0)
            '''
    print(src," ",aux," ",dest)
    if check==aux or check==dest:
        print("YOU BEAUTIFUL GENIUS!!!!!!!!!!!!!")


disks=4
towers(disks)

