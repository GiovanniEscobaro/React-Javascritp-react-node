def analizar_numeros(lista_numeros):
    suma = sum(lista_numeros)
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    promedio = suma / len(lista_numeros)
    
    return suma, mayor, menor, promedio

while True:
    entrada = input("Ingresa números separados por coma: ")
    # Convertimos la cadena a una lista de enteros
    numeros = [int(x.strip()) for x in entrada.split(",")]

 suma, mayor, menor, promedio = analizar_numeros(numeros)

print(f"- Suma: {suma}")
print(f"- Mayor: {mayor}")
print(f"- Menor: {menor}")
print(f"- Promedio: {promedio}")
    
