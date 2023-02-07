class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(raiz):

    def abd(ArvoreBinaria, min_val, max_val):
        if ArvoreBinaria.dado <= min_val:
            return False

        if ArvoreBinaria.dado >= max_val:
            return False

        esquerdo = True
        direito = True

        if ArvoreBinaria.esq is not None:
            esquerdo = abd(ArvoreBinaria.esq, min_val, ArvoreBinaria.dado)
        if ArvoreBinaria.dir is not None:
            direito = abd(ArvoreBinaria.dir, ArvoreBinaria.dado, max_val)

        return esquerdo and direito

    if raiz is None:
        return True
    min_val = float("-inf")
    max_val = float("inf")
    return abd(raiz, min_val, max_val)

raiz = ArvoreBinaria(2, ArvoreBinaria(1), ArvoreBinaria(3))
print(constituiArvoreBinariaDeBusca(raiz))

raiz = ArvoreBinaria(10, ArvoreBinaria(8), ArvoreBinaria(28, ArvoreBinaria(26), ArvoreBinaria(30)))
print(constituiArvoreBinariaDeBusca(raiz))

raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))