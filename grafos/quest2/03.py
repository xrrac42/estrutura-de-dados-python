def insereV(dicionario, vertice):
    if vertice not in dicionario:
        dicionario[vertice] = []

def insereA(dicionario, vertice, aresta, peso=0):
    if vertice in dicionario:
        for i in range(0, len(aresta), 2):
            dicionario[vertice].append(aresta[i])

def bfs(grafo, vertice_fonte, vertice_achar):
    contador = 0
    visitados = []
    listas = []
    visitados.append(vertice_fonte)
    listas.append(vertice_fonte)

    while listas:
        if vertice_achar not in visitados:
            s = listas.pop(0)            
        for vizinho in grafo[s]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                listas.append(vizinho)

        return visitados

numero_de_comparacoes = int(input())
grafo = {}

for _ in range(numero_de_comparacoes):
    linha = input().split()
    insereV(grafo, linha[0])
    insereA(grafo, linha[0], linha[2:])

eu, mussum = input().split()
valor = bfs(grafo, eu, mussum)

if len(valor) < 1:
    print("Forevis alonis...")
else:
    print(len(valor)-1)