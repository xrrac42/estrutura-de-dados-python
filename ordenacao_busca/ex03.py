parciais = {}
for i in range(int(input())):
    nome = input()
    tempo = map(float,input().split())
    tempo = sum(tempo)
    tempo = round(tempo,3)
    parciais[nome] = tempo

print(sorted(parciais, reverse= True))