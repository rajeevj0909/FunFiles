#fizzbuzz v1
'''
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print ("Buzz")
    else:
              
        print(i)

'''
# increasing re-useability
1
'''
start = 0
end = 101
multipleOne = 3
multipleTwo = 5
outputOne = "Fizz"
outputTwo = "Buzz"
for i in range(start,end):
    if i%multipleOne == 0 and i%multipleTwo == 0:
        print (outputOne + outputTwo)
    elif i%3 ==0:
        print(outputOne)
    elif i%5 ==0:
        print (outputTwo)
    else:
              
        print(i)
    
'''

#condensing the messs

'''

def FizzBuzz(start,end,multipleOne,multipleTwo,outputOne,outputTwo):
    for i in range(start,end):
        if i%multipleOne == 0 and i%multipleTwo == 0:
            print (outputOne + outputTwo)
        elif i%3 ==0:
            print(outputOne)
        elif i%5 ==0:
            print (outputTwo)
        else:
                  
            print(i)


FizzBuzz(0,101,3,5,"Fizz","Buzz")

'''

#using classes?

class sequence:
    def __init__(self,start,end):
        self.start = start
        self.end =end
    def FizzBuzz(self,multipleOne,multipleTwo,outputOne,outputTwo):
        for i in range(self.start,self.end):
            if i%multipleOne == 0 and i%multipleTwo == 0:
                print (outputOne + outputTwo)
            elif i%3 ==0:
                print(outputOne)
            elif i%5 ==0:
                print (outputTwo)
            else:
                      
                print(i)
x = sequence(1,101)
sequence.FizzBuzz(self,3,5,"Fizz","Buzz")

# FizzBuzz(0,101,3,5,"Fizz","Buzz") this will return fizzbuzz is not a class

#potentially ask them to replay the sequence
    

        
