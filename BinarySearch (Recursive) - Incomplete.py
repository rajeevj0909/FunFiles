def binarySearch (arr, l, r, x): 
    if """_____""": 
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            """_____""" 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch("""_____""") 
  
    else: 
        return -1
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    """_____"""
else: 
    """_____"""
