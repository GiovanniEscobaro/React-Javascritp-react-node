# Lista
lista=[8,7,10,5,1,7,5,6,2,1,4,3,2,9,8,10]
# Se crea variable para almacenas los duplicados
lista_sin_duplicados=[]
lista_sin_duplicados1=[]

# de recore la lista y se adciona y si no esta la lista de duplicados
for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

# Se imprime la lista si duplicados esta el orde de menor a mayor y el orden de menor a mayor
print(f'Lista original {lista}')
print(f'sin duplicados {lista_sin_duplicados}')
lista_sin_duplicados.sort()
print(f'de menor a mayor {lista_sin_duplicados}')
lista_sin_duplicados.sort(reverse=True)
print(f'De myao a menor {lista_sin_duplicados}')    

lista_sin_duplicados1=list(dict.fromkeys(lista))

print(f'Fromula mejora de duplicados {lista_sin_duplicados1}')
lista=lista_sin_duplicados1
print(f'lista original reeplazada {lista}')
