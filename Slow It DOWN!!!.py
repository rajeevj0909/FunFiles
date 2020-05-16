import time
st=time.time()#read system time before
for i in range(1000):
    print(i*5/3+100)#random nonsense processing
en=time.time()#read system time after
t= en-st #calculate the difference b/w end and start time
print("Process completed in {} seconds".format(t) )

