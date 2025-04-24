numeros=[]
n=1
while True:
    numero=int(input(f'Digete es primer numero y 0 para terminar{n}: '))
    n+=1
    if numero==0:
        break
    numeros.append(numero)
  

print(len(numeros))

suma=sum(numeros)
mayor=max(numeros)
menor=min(numeros)
promedio=suma/len(numeros)

print(f'La suma es: {suma}, el promedio es: {promedio}, el mayor es: {mayor} , el menor es {menor}')






