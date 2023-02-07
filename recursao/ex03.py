soma = 0
n = int(input())
numeros = []
for i in range(1,n+1):
    valor = (2*i) -1
    numeros.append(valor)
    soma += valor
 
for count, j in enumerate(numeros):
    if count +1 <len(numeros):
        print(f'{numeros[count]} + soma({numeros[count+1:]})')
print(numeros[-1])
print('---------------')
print(f'{n} ** 2 == {soma}')