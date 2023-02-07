from collections import deque

class Fila:
    def __init__(self):
        self.items = []
    def push_begin (self,item):
        self.items.insert(0, item)
    def push_final(self,item):
        self.items.append(item)
    def pop_begin(self):
        if len(self.items) > 0:
            del(self.items[0])
        else:
            pass
    def view_begin(self):
        return self.items[0]
    def pop_final(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            pass
    def view_final(self):
        indice = len(self.items)
        return self.items[indice-1]    
        
    def view(self):
        return self.items
        
f = Fila()

while True:
    opcao = input().split()
    if opcao[0] == 'I':
        f.push_begin(opcao[1])
    if opcao[0] == 'F':
        f.push_final(opcao[1])
    if opcao[0] == 'X':
        for i in f.view():print(i)
        break
    if opcao[0] == 'D':
        print(f.view_begin())
        f.pop_begin()
    if opcao[0] == 'P':
        print(f.view_final())
        f.pop_final()  
        
    
