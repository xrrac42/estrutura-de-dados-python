from collections import defaultdict

class Fila:
    def __init__(self) :
        self.items = {}
    def push(self,item,valor):
            self.items[item] = valor
    def delete(self,item):
        self.items.pop(item)
        
    def view(self):
        indices = list(self.items.keys())
        indices = reversed(indices)
        total = sum(self.items.values())
        for i in indices:
            print(f'{i}: R$ {self.items[i]:.2f}')
        print('----------------------')
        print(f'{len(self.items)} item(ns): R$ {total:.2f}')

f = Fila()
            
while True:
    item_valor = input().split()
    if item_valor[0] == 'fim':
        f.view()
        break
    else:
        if item_valor[0] == '-':
            f.delete(item_valor[1])
        else:
            item = item_valor[0]
            valor = float(item_valor[1])
            f.push(item,valor)
    