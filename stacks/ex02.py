class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            pass
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            pass
        
    def size(self):
        return len(self.items)  
    
s = Stack()