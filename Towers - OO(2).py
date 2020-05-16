#import time
class tower():
    def __init__(self, src, aux, dest, counter, reciept, disks):
        self.src = src
        self.aux = aux
        self.dest = dest
        self.counter=counter
        self.reciept=reciept
        self.disks=disks
  
    def towers(self):
        for disk in range(self.disks):
            count=self.disks-disk
            self.src.insert(0,count)
        check=[]
        for n in self.src:
            check.append(n)
        s=(len(self.src))-1
        a=(len(self.aux))-1
        d=(len(self.dest))-1
        self.src.pop(s)
        self.aux.pop(a)
        self.dest.pop(d)
        print(self.src," ",self.aux," ",self.dest)
        self.src.insert(s,99)
        self.aux.insert(a,88)
        self.dest.insert(d,99)
        self.reciept=[0]
        self.counter=0
        ##START OF GAME
        if self.disks%2==1:
            top=self.src[0]
            self.dest.insert(0,top)
            self.src.pop(0)
            self.reciept.insert(0,"t1-3")
            for move in range(2**self.disks-2):
                print(self.reciept)
                self.counter=self.counter+1
                s=(len(self.src))-1
                d=(len(self.dest))-1
                a=(len(self.aux))-1
                self.src.pop(s)
                self.dest.pop(d)
                self.aux.pop(a)
                print(self.src," ",self.aux," ",self.dest)
                self.src.insert(s,99)
                self.dest.insert(d,88)
                self.aux.insert(a,99)
                if ((len(self.dest)==0)or (self.dest[0]>self.src[0]))and ((self.src[0])%2!=(self.dest[0])%2)and (len(self.src)>0)and(self.reciept[0]!="t3-1"):
                    self.reciept.insert(0,"t1-3")
                    top=self.src[0]
                    self.dest.insert(0,top)
                    self.src.pop(0)
                elif ((len(self.aux)==0)or (self.aux[0]>self.src[0]))and ((self.src[0])%2!=(self.aux[0])%2)and (len(self.src)>0)and(self.reciept[0]!="t2-1"):
                    self.reciept.insert(0,"t1-2")
                    top=self.src[0]
                    self.aux.insert(0,top)
                    self.src.pop(0)
                elif ((len(self.aux)==0)or (self.aux[0]>self.dest[0]))and ((self.dest[0])%2!=(self.aux[0])%2)and (len(self.dest)>0)and(self.reciept[0]!="t2-3"):
                    self.reciept.insert(0,"t3-2")
                    top=self.dest[0]
                    self.aux.insert(0,top)
                    self.dest.pop(0)
                elif ((len(self.src)==0)or (self.src[0]>self.dest[0]))and ((self.dest[0])%2!=(self.src[0])%2)and (len(self.dest)>0)and(self.reciept[0]!="t1-3"):
                    self.reciept.insert(0,"t3-1")
                    top=self.dest[0]
                    self.src.insert(0,top)
                    self.dest.pop(0)
                elif ((len(self.dest)==0)or (self.dest[0]>self.aux[0]))and ((self.aux[0])%2!=(self.dest[0])%2)and (len(self.aux)>0)and(self.reciept[0]!="t3-2"):
                    self.reciept.insert(0,"t2-3")
                    top=self.aux[0]
                    self.dest.insert(0,top)
                    self.aux.pop(0)
                elif ((len(self.src)==0)or (self.src[0]>self.aux[0]))and ((self.aux[0])%2!=(self.src[0])%2)and (len(self.aux)>0)and(self.reciept[0]!="t1-2"):
                    self.reciept.insert(0,"t2-1")
                    top=self.aux[0]
                    self.src.insert(0,top)
                    self.aux.pop(0)
        else:
            top=self.src[0]
            self.aux.insert(0,top)
            self.src.pop(0)
            self.reciept.insert(0,"t1-2")
            for move in range(2**self.disks-2):
                self.counter=self.counter+1
                s=(len(self.src))-1
                a=(len(self.aux))-1
                d=(len(self.dest))-1
                self.src.pop(s)
                self.aux.pop(a)
                self.dest.pop(d)
                print(self.src," ",self.aux," ",self.dest)
                self.src.insert(s,99)
                self.aux.insert(a,88)
                self.dest.insert(d,99)
                if ((len(self.dest)==0)or (self.dest[0]>self.src[0]))and ((self.src[0])%2!=(self.dest[0])%2)and (len(self.src)>0)and(self.reciept[0]!="t3-1"):
                    self.reciept.insert(0,"t1-3")
                    top=self.src[0]
                    self.dest.insert(0,top)
                    self.src.pop(0)
                elif ((len(self.aux)==0)or (self.aux[0]>self.src[0]))and ((self.src[0])%2!=(self.aux[0])%2)and (len(self.src)>0)and(self.reciept[0]!="t2-1"):
                    self.reciept.insert(0,"t1-2")
                    top=self.src[0]
                    self.aux.insert(0,top)
                    self.src.pop(0)
                elif ((len(self.aux)==0)or (self.aux[0]>self.dest[0]))and ((self.dest[0])%2!=(self.aux[0])%2)and (len(self.dest)>0)and(self.reciept[0]!="t2-3"):
                    self.reciept.insert(0,"t3-2")
                    top=self.dest[0]
                    self.aux.insert(0,top)
                    self.dest.pop(0)
                elif ((len(self.src)==0)or (self.src[0]>self.dest[0]))and ((self.dest[0])%2!=(self.src[0])%2)and (len(self.dest)>0)and(self.reciept[0]!="t1-3"):
                    self.reciept.insert(0,"t3-1")
                    top=self.dest[0]
                    self.src.insert(0,top)
                    self.dest.pop(0)
                elif ((len(self.dest)==0)or (self.dest[0]>self.aux[0]))and ((self.aux[0])%2!=(self.dest[0])%2)and (len(self.aux)>0)and(self.reciept[0]!="t3-2"):
                    self.reciept.insert(0,"t2-3")
                    top=self.aux[0]
                    self.dest.insert(0,top)
                    self.aux.pop(0)
                elif ((len(self.src)==0)or (self.src[0]>self.aux[0]))and ((self.aux[0])%2!=(self.src[0])%2)and (len(self.aux)>0)and(self.reciept[0]!="t1-2"):
                    self.reciept.insert(0,"t2-1")
                    top=self.aux[0]
                    self.src.insert(0,top)
                    self.aux.pop(0)
        
        s=(len(self.src))-1
        a=(len(self.aux))-1
        d=(len(self.dest))-1
        self.src.pop(s)
        self.aux.pop(a)
        self.dest.pop(d)
        print(self.src," ",self.aux," ",self.dest)
        print(str(self.counter+2)+" Moves   " +str(self.disks)+" disks")


disks=int(input("How many disks? Make it an even number pls!"))
src = [99]
aux = [88]
dest = [99]
counter=[]
reciept=0
x=tower(src, aux, dest, counter, reciept, disks)

x.towers()



