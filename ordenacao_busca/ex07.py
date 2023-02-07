
for j in range(int(input())):
    count = 0
    s_union = ''
    count += 1
    if count == 1:
        first = input()
        first = list(first)
        first = sorted(first)
        for k in range(3):
            s = input()
            s_union = s_union + s
        condition = 1
        s_union = list(s_union)
        s_union = sorted(s_union)
        new_first = ''
        for l in s_union:
            if l in first:
                new_first += l
                condition = 1
            else:
                print('You died!')
                condition = 0
                break
        if condition != 0:
            if len(new_first) == len(first):
                print("It's in the box!")
            else:
                if len(new_first) > len(first) and condition ==1:
                    print('You Died!')
                else:
                    bo = ''
                    bo_new = ''
                    for letra in first:
                        if letra not in new_first:
                            bo = bo + letra
                    bo = set(bo)
                    bo = list(bo)
                    bo = sorted(bo)
                    for n in list(bo):
                        bo_new = bo_new + n
                    
                    print(f'Bora ralar: {bo_new}')
