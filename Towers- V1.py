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
    
   
    ##START OF GAME
    for move in range(2**disks-1):
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
            
    print(src," ",aux," ",dest)
    if check==aux or check==dest:
        print("YOU BEAUTIFUL GENIUS!!!!!!!!!!!!!")


disks=4
towers(disks)

