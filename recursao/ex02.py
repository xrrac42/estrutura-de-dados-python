def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_2(n):
    chamadas = []
  
    ultimo=1
    penultimo=1

    if (n==1) or (n==2):
        chamadas.append(n)
        print("1")
    else:
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            chamadas.append(n)
    return chamadas
print(fibonacci_2(4))

