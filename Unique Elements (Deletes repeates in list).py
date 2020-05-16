def unique_elements(numbers):
    new=[]
    for i in numbers:
        if i not in new:
            new.append(i)
    print(new)



numbers=["1","2","2","2","3","3","3","3","3","3","4","4","2","4","4","5","2","5","4","5","6","7","7"]
unique_elements(numbers)


