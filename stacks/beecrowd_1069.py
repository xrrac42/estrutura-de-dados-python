class Stack:
    def __init__(self):
        self.items= []
    
    def push(self,item):
        self.items.insert(0,item)
        
    def pop(self):
        if len(self.items) > 0:
            self.items.pop(0)
            
            
    def size(self):
        return len(self.items)    


s = Stack()
for _ in range(int(input())):
    count = 0     
    entrada = input()
    for i in entrada:
        if i == '<':
            s.push(i)
        if i == '>':
            s.pop()
            count += 1
    print(count)

