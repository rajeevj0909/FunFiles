L1 = ["blob,blip","blip,blip","blob,blip"]
L2 = ["blob,blob,blob,blob,blip","blip,blob,blip,blob,blip,blob","blob,blob,blob","blip,blip"]
L3 = [];
word = "blob"
def blobby(List):
    print(List)
    #an array to hold the output of the function
    output = [];

    #looping through the lists
    for i in range(0,len(List)):
        subList = List[i].split(",")
        count = 0;
        
        for j in range(0,len(subList)):
            
            if subList[j] == word:
                count = count +1
                
        output.append(count)
        
    
    count =0 ;
    #summing up the number of blobs
    for Q in range(0,len(output)):
        count = count + output[Q];

    output.append(count);
    

    #print it out in the correct format
    strOutput ="";

    for k in range (0,len(output) -1):
        strOutput = strOutput + str(output[k]) + "|";
    strOutput = strOutput + str(output[-1]);
    

    return strOutput;

print(blobby(L1))
print(blobby(L2))
print(blobby(L3))
    
    
