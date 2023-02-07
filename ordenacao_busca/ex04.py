notas = [[],[],[],[],[],[]]

for i in range(int(input())):
    nota = input()
    if nota[0:2] == 'SS':
        notas[0].append(nota[3:])
    if nota[0:2] == 'MS':
        notas[1].append(nota[3:])
    if nota[0:2] == 'MM':
        notas[2].append(nota[3:])
    if nota[0:2] == 'MI':
        notas[3].append(nota[3:])
    if nota[0:2] == 'II':
        notas[4].append(nota[3:])
    if nota[0:2] == 'SR':
        notas[5].append(nota[3:])

for j in range(len(notas)):
    if j == 0:
        mencao = 'SS'
    if j == 1:
        mencao = 'MS'
    if j == 2:
        mencao = 'MM'
    if j == 3:
        mencao = 'MI'
    if j == 4:
        mencao = 'II'
    if j == 5:
        mencao = 'SR'
    if len(notas[j]) > 0:
        notas[j].sort()
        for k in notas[j]:
            print(f'{mencao} {k}')