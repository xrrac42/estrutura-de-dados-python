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
    def remove_itens(self,item):
        self.items = [value for value in self.items if value != item ]
    def count(self,item):
        return self.items.count(item)    
    def remove_positional(self,indice):
        self.items.pop(indice)
    def switch_item(self,item,new_item):
        indice = self.items.index(item)
        self.items[indice] = new_item
       
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
    if opcao[0] == 'V':
        print(f.count(opcao[1]))
        f.remove_itens(opcao[1])
    if opcao[0] == 'E':
        print(opcao[1])
        f.remove_positional(int(opcao[1]))

    if opcao[0] == 'T':
        f.switch_item(opcao[1],opcao[2])
    if opcao[0] == 'C':
        print(f.count(opcao[1]))
            

