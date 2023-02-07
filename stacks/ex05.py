def duplicata(string):
    s = list()
    for i in string:
        if i == ')':

            topo = s.pop()
            elementos = 0
            while topo != '(':

                elementos += 1
                topo = s.pop()

            if elementos < 1:
                return 'A expressão possui duplicata'
        else:
            s.append(i)

    return 'A expressão não possui duplicata.'



for _ in range(int(input())):
    expressao = input()
    print(duplicata(expressao))

