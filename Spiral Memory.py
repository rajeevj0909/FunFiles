count=3
circum=1
total=1
cumltve=10
pathfinder=int(input("What number?"))

while pathfinder>cumltve:
  count=count+1
  circum=circum+2
  smaller=cumltve
  total=((circum+2)*2)+(circum*2)
  print(cumltve,end="-")
  cumltve=cumltve+total
  print(cumltve-1)

print("\n")
count=count-1
quad=(4*(count*count))
lin=(-4*count)
print("Higher No.")
larger=quad+lin+1
print(larger)
length=(circum+1)/2
print("Steps to circum")
print(length)
side=((length-1)*2)+3
print("Side")
print(side)
print("\n")
print("Smaller No.")
print(smaller)
print("")
middlelft=(smaller)+(length)-1
print("Middle NO. ON LEFT")
print(middlelft)
print("Middle NO. ON BOTTOM")
middlert=(larger)-(length)
print(middlert)
print("THE STEPS")
print(length+(pathfinder-middlelft))
  
