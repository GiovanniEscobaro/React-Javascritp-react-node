lista=[]
    #Se pide los numero por el cliente
while True:
        DigiteNumero=input('Digete numero o palabar (para detener digita salir) : ')
            # Si ese salir
        if DigiteNumero=="salir":
                print("Saliendo")
                # ternima el whiler
                break
            #lo adciona a la lista
        else:
                numero=DigiteNumero
                lista.append(numero)
print(lista)
lista_inveirtia=[]

# lista invertida
for i in range(len(lista)-1,-1,-1) :
    lista_inveirtia.append(lista[i])
    
print(f'Lista invertida: {lista_inveirtia}')


