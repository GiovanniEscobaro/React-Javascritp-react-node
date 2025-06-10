#Pide al usuario un numero y muestra su taba de multuplicar del 1 a 10
numero=int(input('Digita en numero: '))
multiplicacion=1
for i in range(1,11):
    multiplicacion=numero*i
    print(f'{numero} * {i} = {multiplicacion}')
