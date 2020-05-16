import time
s = [5,4,3,2,1]
a = []
d = []
end_state = [5,4,3,2,1]
while d != end_state:
    time.sleep(2)
    if len(d) == 0:
        disk = s.pop()
        d.append(disk)
    elif len(s) == 0:
        disk = d.pop()
        s.append(disk)
    else:
        if s[len(s)-1] < d[len(d)-1]:
            disk = s.pop()
            d.append(disk)
        elif d[len(d)-1] < s[len(s)-1]:
            disk = d.pop()
            s.append(disk)
    print(s,a,d)
    time.sleep(1)
    if d == end_state:
        break
    if len(a) == 0:
        disk = s.pop()
        a.append(disk)
    elif len(s) == 0:
        disk = a.pop()
        s.append(disk)
    else:
        if s[len(s)-1] < a[len(a)-1]:
            disk = s.pop()
            d.append(disk)
        elif a[len(a)-1] < s[len(s)-1]:
            disk = a.pop()
            s.append(disk)
    
    print(s,a,d)
    time.sleep(1)
    if d == end_state:
        break
    
    if len(a) == 0:
        disk = d.pop()
        a.append(disk)
    elif len(d) == 0:
        disk = a.pop()
        d.append(disk)
    else:
        if d[len(d)-1] < a[len(a)-1]:
            disk = d.pop()
            a.append(disk)
        elif a[len(a)-1] < d[len(d)-1]:
            disk = a.pop()
            d.append(disk)
    
    print(s,a,d)
    time.sleep(1)
    

