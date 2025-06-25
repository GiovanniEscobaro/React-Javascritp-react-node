numero_palabras=int(input('Digite en numero de palabras: '))
palabras=[]
contador=1
while numero_palabras>=contador:
    contador+=1
    palabra=input(' Digite la palabra: ')
    palabras.append(palabra)
print(palabras)

# 
palabra_larga=""
longitud_larga=0
for palabra in palabras:
    if len(palabra)>longitud_larga:
        longitud_larga=len(palabra)
        palabra_larga=palabra
print(f'La palabra mas larga es {palabra_larga} con un logitud de {longitud_larga}' )


# Lo como se optimazae el codigo

longitud_maximo=max(len(p)for p in palabras)
palabra_larga=longitud_maximo
