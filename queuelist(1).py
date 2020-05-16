global queue
queue = []

def dequeue():
    return queue.pop()
def enqueue(data):
    queue.append(data)
def size():
    return(len(queue))
def isEmpty():
    if queue == []:
        return True
    else:
        return False
def front():
    return queue[0]

print(isEmpty())
queue = [1,2,3,4,5]
print(queue)
dequeue()
print(queue)
enqueue(5)
print(queue)
print(size())
print(isEmpty())
print(front())
