class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         push_input=input("What do you want to add?")
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack()
example=["Hi","I","am","Rajeev"]
print(s.isEmpty())
print(s.push(example))
print(s.pop(example))
print(s.seek(example))
print(s.size(example))
#print((example))
