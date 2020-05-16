list1=[1,0,0,6,2,0,1,9]

pivot=len(list1)-1#Pivot always at end of list
pointer=0 #Pointer always at start
pivot_reached=False#Checks when a pivot is found

def quickSort(list1,pivot,pointer,pivot_reached):
    pivot=len(list1)-1
    pointer=0
    #While the pointer and pivot aren't at same item
    while pivot_reached==False:
        print(list1)
        print("Pivot: ",list1[pivot],"Pointer: ",list1[pointer])
        #If the pointer is on the left side
        if pointer<pivot:
            #If the value is smaller, it passes
            if list1[pointer]<list1[pivot]:
                pointer=pointer+1
            else:
                #If not it swaps the items and pointers
                print("SWAP pointers Left")
                #Swap pointers
                temp=pivot
                pivot= pointer
                pointer=temp
                #Swap items
                list1.insert(pivot,list1[pointer])
                list1.insert(pointer+1,list1[pivot+1])
                list1.pop(pivot+1)
                list1.pop(pointer+1)
        #If the pointer is on the right side of pivot
        elif pointer>pivot:
            #If the value is larger, it passes
            if list1[pointer]>list1[pivot]:
                pointer=pointer-1
            else:
                #If not it swaps the items and pointers
                print("SWAP pointers Right")
                #Swap pointers
                temp=pivot
                pivot= pointer
                pointer=temp
                #Swap items
                list1.insert(pivot,list1[pointer])
                list1.insert(pointer+1,list1[pivot+1])
                list1.pop(pivot+2)
                list1.pop(pointer)
                pointer=pointer+1
        #When the whole list is done and the pointers touch
        if pivot==pointer:
            print(list1)
            pivot_reached=True
  
    #When the first pivot is found
    if pivot_reached==True:
            print("PIVOT FOUND")
            pivot_reached=False
            #Checks if there is 2 or more items to the left of the found pivot
            if pivot>1:
                print("Left List Sort:")
                #This inserts the new left list into quicksort
                new_list=quickSort(list1[0:pivot],pivot,pointer,pivot_reached)
                #Removes the unsorted part
                del list1[0:pivot]
                #Replaces it with the sorted part
                for num in range(len(new_list)-1,-1,-1):
                    list1.insert(0,new_list[num])
                    
            #Checks if there is 2 or more items to the right of the found pivot
            if pivot<len(list1)-2:
                print("Right List Sort:")
                #This inserts the new right list into quicksort
                new_list=quickSort(list1[pivot+1:len(list1)],pivot,pointer,pivot_reached)
                #Removes the unsorted part
                del list1[pivot+1:len(list1)]
                #Replaces it with the sorted part
                for num in range(0,len(new_list)):
                    list1.insert(len(list1),new_list[num])
    return(list1)
    print("END")
    
list1=quickSort(list1,pivot,pointer,pivot_reached)
print(list1)
'''
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
'''
