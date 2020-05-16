Input = "pwwkew"
subStr = [];
for i in range(0,len(Input)):
    for j in range(0,len(Input)):
        sub = Input[i:j+1]
        if (sub in subStr) == False:
            subStr.append(sub);

print(subStr);
subStr.sort(key=len, reverse = True);
print(subStr);


longSub = "";
for i in range (0,len(subStr)):
    found = True;
    tempStr = list(subStr[i]);
    for j in range(0,len(tempStr)):
        
        if subStr[i].count(tempStr[j]) > 1:
            found = False;
            break;
        
    if found == True:
        print(subStr[i])
        break;
