class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # Implemente este método.
         self.items.insert(0,item)
      
    def pop(self):
       # Implemente este método.
       self.items.pop(0)
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
