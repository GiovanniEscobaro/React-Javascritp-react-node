
# se define funcion

    # Variable listas
lista=[]
    #Se pide los numero por el cliente
while True:
        try:
            DigiteNumero=input('Digete numero(para detener digita salir) : ')
            # Si ese salir
            if DigiteNumero=="salir":
                print("Saliendo")
                # ternima el whiler
                break
            #lo adciona a la lista
            elif DigiteNumero.isdigit():
                numero=int(DigiteNumero)
                lista.append(numero)
            else:
                print("Error: La entrada no es un numero")
        except ValueError:
            print("Error: La entrada no es numero entero")
print(f'Lista de numeros: {lista}')
    

contador=0
sumatotal=0
promedio=0
mayor=lista[0]
menor=lista[0]
for numero in lista:
    sumatotal+=numero
    contador+=1
    if numero <= menor:
         menor=numero
    elif numero> mayor:
         mayor=numero

print(f'La numero mayor:{mayor}')
print(f'El numero menor: {menor}')
         
pomedio=sumatotal/contador
print(f'La suma total en de : {sumatotal}')
print(f'El promedio es : {pomedio}')

numeromayor=lista[0]
numeromenor=lista[0]
lista_mayor=max(lista)
lista_menor=min(lista)

print(f'Con el nuevo metodo en mayro es: {lista_mayor} y el menor es: {lista_menor}')












      