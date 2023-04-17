cont = ("", "uma", "duas","três","quatro", "cinco","seis", "sete", "oito","nove", "dez")

num = int(input())

c=num // 100
d=(num % 100) // 10
u= (num% 100) % 10

##centenas
if c == 0:
    pass
if c == 1:
    print (cont[c], "centena",end="")
    if d >= 1 and u < 1:
        print(" e ",end="")
    if d>=1 and u>=1:
        print(", ",end="")
if c > 1:
    print (cont[c], "centenas",end="")
    if d >= 1 and u < 1:
        print (" e ",end="")
    if d>=1 and u>=1:
        print(", ",end="")
    
##dezenas
if d == 0:
    if u >=1 and c > 0:
        print(" e ",end="")
if d == 1:
    print (cont[d],"dezena", end="")
    if u >= 1:
        print (" e ",end="")
if d > 1:
    print (cont[d],"dezenas",end="")
    if u >= 1:
        print (" e ",end="")
    else:
        pass

###unidades
    
if u > 1:
    print (cont[u], "unidades",end="")
    
    
if u == 0:
    pass

if u == 1 and d >= 1 and c >= 1:
    print (cont[u],"unidade",end="")

if u == 1 and d < 1 or u==1 and c < 1:
    print(cont[u],"unidade",end="")

print(".")
