#Crea una función que calcule el factorial de un número entero positivo.

Numero=int(input('Numero para calcular Factorial: '))
factorial=1
if Numero>0:
    for i in range(1,Numero+1):
        factorial=factorial*i

print (f'El factorial de {Numero} es {multiplica}')