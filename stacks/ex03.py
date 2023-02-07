class Stack:
    def __init__(self):
        self.items = []
    
    def length(self):
        return len(self.items)

    def push(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items[0:self.items.index(stop)]) + 1

    def total(self):
        return sum(self.items[0:self.items.index(stop)]) + stop


s = Stack()

while True:
    n = int(input())
    if n == 0:
        break
    s.push(n)

stop = int(input())

if s.length() == 0:
    print(f'Peso retirado: 0')
    print(f'Anilhas retiradas: 0')
    print(f'Peso total movimentado: 0')
else:
    for i in s.items:
        if i == stop:
            print(f'Peso retirado: {i}')
            break
        print(f'Peso retirado: {i}')


    print(f'Anilhas retiradas: {s.size()}')
    print(f'Peso total movimentado: {s.total()}')
