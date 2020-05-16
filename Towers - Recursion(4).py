#Runs the funct
def towers(disks,src,aux,dest,counter,reciept,check):
    #Increments a counter
    counter=counter+1
    #Finds the positions of the last item
    s=(len(src))-1
    a=(len(aux))-1
    d=(len(dest))-1
    #Takes off the last number from every list before printing
    src.pop(s)
    aux.pop(a)
    dest.pop(d)
    #Print the lists
    print(src," ",aux," ",dest)
    #Adds the 3 numbers back into the list at the end
    src.insert(s,99)
    aux.insert(a,88)
    dest.insert(d,99)
    #The function that swaps the disks from tower to tower
    def move(change,come,go):
        #Creates a reciept for all the moves made
        reciept.insert(0,change)
        #Removes disk from one list
        top=come.pop(0)
        #Adds disk to another list
        go.insert(0,top)
    #Base case, checks if 
    if check==dest:
        #Print a final message
        print(str(counter+1)+" Moves   " +str(disks)+" Disks")
        #The function which ends the recursion
        return("DONE!!!!")
    #VALIDATION CHECKS FOR (empty list),(the bigger disk on 2 towers), (even on odd), (checks if there is something in the list), (Adds a reciept)
    elif ((len(dest)==0)or (dest[0]>src[0]))and ((src[0])%2!=(dest[0])%2)and (len(src)>0)and(reciept[0]!="t3-1"):
        #Runs the function to do the moves
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

#Input of disks    
disks=int(input("How many disks? Make it an even number pls!"))
#Lists created
src = [99]
aux = [88]
dest = [99]
#Create src using disks
for disk in range(disks):
    count=disks-disk
    src.insert(0,count)
#Create checker
check=[]
for n in src:
    check.append(n)
#Prints list
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
#Creates list, counter
reciept=[0]
counter=0
##START OF GAME
#Checks if odd
if disks%2==1:
    top=src[0]
    dest.insert(0,top)
    src.pop(0)
    reciept.insert(0,"t1-3")
#Checks if even
else:
    top=src[0]
    aux.insert(0,top)
    src.pop(0)
    reciept.insert(0,"t1-2")
    even=True
#Runs function
towers(disks,src,aux,dest,counter,reciept,check)





