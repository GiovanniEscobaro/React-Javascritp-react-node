numeros=[4,1,3,8,9,10,6,10,6,11]
IndeciNumeros=len(numeros)
ordenar=[]
for i in range(len(numeros)):
    k=0
    l=0
    j=0
    tamaño=len(numeros)-1
    menor=numeros[0]
    for j in range(len(numeros)-1):
        
        if numeros[j]<=menor:
            menor=numeros[j]
            l=k
        k+=1    
    orden=numeros[l]
    ordenar.append(orden)
    del numeros[l]
print(ordenar)

        

