def insertionSort(alist):
   for index in range(1,len(alist)):
     temp = alist[index]
     position = index
     while """_____""" and alist[position-1] > temp:
         alist[position] = alist[position-1]
         """_____"""
     alist[position] = temp
   return """_____"""

unsorted_list = [54,26,93,17,77,31,44,55,20]
print("Before:", unsorted_list)
sorted_list = insertionSort(unsorted_list)
print("After:", sorted_list)
