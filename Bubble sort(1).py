def bubblesort(randomlist): #defines the function for later use, named bubblesort
    print(randomlist)
    for passes in range(len(randomlist)-1,0,-1): # passnum defines the number of passes in the list, allows the system to recognise when the process is complete. Specifies the length of the list - 1, specifying that the number of passes will be 1 less than the overall length of the list. Reduces by 1 with each complete pass because the code no longer needs to assess the final numbers. Stops at 0
        for number in range(passes): #assesses the list, going through each individual number in the list
            if randomlist[number]>randomlist[number+1]: #process determines if the value in the list is greater than the next value in the list
                sort = randomlist[number] #stores the value temporarily, called sort due to it being the number being sorted
                randomlist[number]=randomlist[number+1] #changes the value being assessed to the next value
                randomlist[number+1] = sort #re-implements the value in the next position, thus putting the two items in the correct order (these three steps re-arrange the two numbers to the correct order of size)
                print(randomlist)

randomlist=[11,8,43,67,2,89,77,23,50,1] #defines the array to be used
bubblesort(randomlist) #runs the process for the specified array


        
        
