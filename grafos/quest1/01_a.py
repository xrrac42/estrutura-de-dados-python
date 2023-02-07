class Grafo:


    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        # estou pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = 1  #trocar = por += ser for grafo múltiplo

        # self.grafo[v-1][u-1] = 1 

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


g = Grafo(3)
g.adiciona_aresta(2,3)
g.adiciona_aresta(2,1)
g.adiciona_aresta(1,2)
g.adiciona_aresta(3,1)
g.adiciona_aresta(3,2)
g.mostra_matriz()