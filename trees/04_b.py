class Nodo:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
lista = []

def sort(raiz):
    if not raiz:
        return
    sort(raiz.esquerda)
    lista.append(raiz.chave),
    sort(raiz.direita)
def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)
n2 = []         
n = int(input())
n2.extend(map(int,input().split()))
raiz = Nodo(n2[0])
for chave in n2[1:]:
    nodo = Nodo(chave)
    insere(raiz, nodo)
sort(raiz)
# indice = lista.index(n2[0])
# lista_esq = (len(lista[0:indice]))
# lista_dir = len(lista[indice:])

# if lista_dir > lista_esq:
#   print(lista_dir-1)
# else:
#   print(lista_esq-1)


def heigth(raiz):
    if raiz is None:
        return 0
    return max(heigth(raiz.esq), heigth(raiz.dir)) + 1


def mostra_arvore_e_altura(raiz):
    altura = heigth(raiz)-1
    if altura == -1:
        altura = 0
    sort(raiz)
    print('')
    print(f'altura:{altura}')   
mostra_arvore_e_altura(raiz)