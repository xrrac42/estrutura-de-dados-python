valores = {}

while True:
    n = int(input())
    if n== 0:
        break
    for i in range(n):
        s = input().split()
        valores[s[0]] = float(s[2])
    valores = sorted(valores, reverse= True)
    for j in valores:
        print(f'{j}',end=' < ')
    
