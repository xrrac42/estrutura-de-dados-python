from pickle import TRUE


graph = {}

def is_cicle(first,last,size = 0 ):
    if size > len(graph.keys()):
        return False
    if first == last and size != 0:
        return True
    for anything in graph[first]:
        if is_cicle(anything,last, size +1):
            return True
    return False         
    

for i in range(int(input())):
    id_a_vn = input().split()
    graph[id_a_vn[0]] = id_a_vn[2:]

anything2 = True
for j in graph.keys():
    count = 0
    if is_cicle(j,j):
        anything2 = False
        print('Hoje tem!')
        break
else:
    print('... que ama ninguem.')


