def getElementById(raiz, id):
    elementos = []
    for i in raiz.keys():
        if i == id:
            
            elementos.append(i)
    for j in raiz.values():
        if j == id:
            elementos.append(i)       
    return(elementos) 

raiz = {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}
print(sorted(getElementById(raiz, 'H1')))


