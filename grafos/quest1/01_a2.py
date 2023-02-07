class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v, peso, direcao): 
        if direcao == 'D':
            self.grafo[u-1][v-1] = peso
        if direcao == 'N':
            self.grafo[u-1][v-1] = peso
            self.grafo[v-1][u-1] = peso


    def view_matriz(self):
        for lin in self.grafo:
            for col in lin:
                print(f"{col:4.0f}", end="")
            print()



v_a_d = input().split()
g = Grafo(int(v_a_d[0]))

for i in range(int(v_a_d[1])):
    u,v, p = map(int,input().split()) 
    g.add_aresta(u, v, p, v_a_d[2])

g.view_matriz()
