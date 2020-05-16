file=open("A Maze of Twisty Trampolines.txt","r")
list1=[]
for line in file:
  line=int(line)
  list1.append(line)
steps=0
pointer=0
print(list1)

while pointer<len(list1) and pointer>-1:
        newval=list1[pointer]+1
        mover=list1[pointer]
        list1[pointer]=newval
        pointer=pointer+mover 
        steps=steps+1

print(list1)
print(steps)
