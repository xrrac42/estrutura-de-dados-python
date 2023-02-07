for i in range(int(input())):
    words = []
    acumula = []
    acumula_aux = ''
    new_word = []
    for j in range(0, 4):
        word = input()
        words.append(word)
    for k in words[1:]:
        for l in k:
            acumula.append(l)

    compara = words[0]
    compara = list(compara)
    compara.sort()
    acumula = list(acumula)
    acumula.sort()
    execute = True
    for z in acumula:
        if z not in compara:
            print('You died!')
            execute = False
            break
    if execute == True:    
        acumula_2 = acumula.copy()
        compara_2 = compara.copy()
        for x in acumula:
            if x in compara:
                indice_compara = compara.index(x)
                compara.pop(indice_compara)

        for y in compara_2:
            if y in acumula_2:
                indice_acumula = acumula_2.index(y)
                acumula_2.pop(indice_acumula)

        if len(acumula_2) == 0 and len(compara) == 0:
            print("It's in the box!")
        else:
            if len(compara) > 0 and len(acumula_2) == 0:
                print('You died!')
            else:
                bo = ''
                compara = list(set(compara))
                compara.sort()
                for bora in compara:
                    bo += bora
                print(f'Bora ralar: {bo}')