suma=0
i=0
while True:
    numero=int(input("Ingrese numeros: "))
    if numero==0:
        break

    suma += numero
    i+=1
if numero != 0:
    primedio=suma/i
    print(f"Promedio de los numero es : {primedio}")
else:    
    print(f"No se puede calcular divido por 0")
print(f"La total es: {suma}")




