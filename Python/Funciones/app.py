def saludar():
    print ('Hola esta es un funcion')

saludar()

def saludar(nombre):
    print(f'Hola, {nombre} como estas?')
    
saludar(input('Danos tu nombre : '))

def suma(a,b):
    return a+b

resultado=suma((int(input('Promir numero: '))), (int(input('segundo numero: '))))
print(f'La suma es : {resultado}')
