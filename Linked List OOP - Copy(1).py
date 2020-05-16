class node():
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=pointer

class linkedList():
    def __init__(self,start,nextFree,count):
        self.start=start
        self.nextFree=nextFree
        self.count=count

    def getSize(self):
        return self.count

    #def add(self):

    #def find(self):
        
node2=node(None,None)
node1=node(0,None)


link=linkedList(node1,node2,5)
print(link.getSize())


print("Hello world")
