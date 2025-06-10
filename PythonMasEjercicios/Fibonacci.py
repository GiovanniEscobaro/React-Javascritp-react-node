Numero=(int(input('Digita numero par calcular Fibonacci: ')))


def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]

    secuencia = [0, 1]  # Primeros dos valores de Fibonacci

    for i in range(2, numero):
        siguiente = secuencia[-1] + secuencia[-2]  # Suma de los dos anteriores
        secuencia.append(siguiente)

    return secuencia
print(fibonacci(Numero))
        
