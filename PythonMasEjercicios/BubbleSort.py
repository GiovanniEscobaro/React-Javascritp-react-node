numeros = [4, 1, 3, 8, 9, 6, 5, 10, 6, 11]

# Algoritmo de Bubble Sort
n = len(numeros)
for i in range(n):
    for j in range(n - 1 - i):  # No necesitamos comparar los últimos ya ordenados
        if numeros[j] > numeros[j + 1]:
            # Intercambiar elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)
