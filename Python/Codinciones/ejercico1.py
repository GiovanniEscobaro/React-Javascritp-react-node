suma=0
i=0
while True:
    numero=int(input("Digite el numero y 0 para salir: "))
    if numero==0:
        break
    i+=1
    suma+= numero

if i==0:
    print('no digito ningun numero, ERRROR')
else:
    promedio=suma/i
    print(f'La suma total es : {suma}, numero ingresados {i}, y el promedio es {promedio}')
