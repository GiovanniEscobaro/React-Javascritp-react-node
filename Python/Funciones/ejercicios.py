def suma_promedio():
    
    suma=0
  
    contador=0
    while True:
        numero=int(input('Digite numeros (0 para terminar): '))
        if numero==0:
            break
        suma+= numero
        contador+=1
    if contador>0:
        promedio=suma/contador
        print(f'El promedio de numeros es: {promedio}, cantida de numeros: {contador}, y la suma total es {suma}')
    else:
        print("no digitas numeros")

suma_promedio()





