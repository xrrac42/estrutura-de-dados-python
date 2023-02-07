def peronio(s1,s2):
    for x in range(len(s1)):
        len_prefixo = 0
        if s1[x] != s2[x]:
            break
        else:
            len_prefixo += 1
                
    if len_prefixo > 0:
        print('Acertô, mizerávi!')
        print(len_prefixo)

count = 0
s1 ='super'
s2 ='superhomem'
print(s1[0]== s2[0])


print(count)