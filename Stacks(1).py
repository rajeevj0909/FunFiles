global stack
stack=[]

def push():
        stack.append(data)
        
        
def pop():
        if stack == []:
                print ("Empty, you moron")
        else:
                return stack.pop()
        
def size():
    return(len(stack))

def isEmpty():
    if stack == []:
        return True
    else:
        return False

def peek():
        length = len(stack)
        return (stack[length-1])


stack = [10,20,30,40,50]
data=int(input("What u wanna add?"))
push()
print(stack)
pop()
print(stack)
print(size())
print(isEmpty())
print(peek())
print(stack)
