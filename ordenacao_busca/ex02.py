x = []
n = int(input())
x.extend(input().split(' '))

y = len(x)-len(set(x))
print(y)


