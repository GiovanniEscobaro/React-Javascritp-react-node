numeros=[10,2,1,5,10,1,5,2,8,10,8,9,7,5,6,7,7,9,8,10]
# El numero a buscar al cliente lo registra
digetenumero=int(input("Por favor digete el numero: "))
contador=0
# Donde se si son iguale y el contador aumenta
for numero in numeros:
    if numero==digetenumero:
        contador+=1
# Si se repite el numero de cliente
print(f'El numero: {digetenumero} esta {contador} repetido ')

# Verificar en toda la lista si los numero se duplican y se hace un dicionario.
elmento_repitidos={}
for numero in set(numeros):
    if numeros.count(numero)>1:
        elmento_repitidos[numero]=numeros.count(numero)
        print(f'contaodo {elmento_repitidos}')
print(f'Elementos repedos {elmento_repitidos}')





