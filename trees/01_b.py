def view_tree(raiz, level=0):
    if raiz != None:
        print('__'*level + str(raiz.dado))
        view_tree(raiz.esq, level + 1)
        view_tree(raiz.dir, level+1)


def heigth(raiz):
    if raiz is None:
        return 0
    return max(heigth(raiz.esq), heigth(raiz.dir)) + 1


def mostra_arvore_e_altura(raiz):
    altura = heigth(raiz)-1
    if altura == -1:
        altura = 0
    view_tree(raiz)
    print('')
    print(f'altura:{altura}')
