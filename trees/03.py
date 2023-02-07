# segundaversao
class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificaSimetria(raiz):
    if not raiz:
        return True
    return _verificaSimetria(raiz.esq, raiz.dir)

def _verificaSimetria(esq, dir):
    if not esq and not dir:
        return True
    if not esq or not dir or esq.dado != dir.dado:
        return False
    return _verificaSimetria(esq.esq, dir.dir) and _verificaSimetria(esq.dir, dir.esq)

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))
 	
raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

 	

False

raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))
print(verificaSimetria(raiz))