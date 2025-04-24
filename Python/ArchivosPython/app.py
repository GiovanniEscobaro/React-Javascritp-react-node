
#Escribe un Archivo crea y reemplaza
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Otra linea\n")
#✅ Agregar sin borrar (append):
with open("archivo.txt", "a") as archivo:
    archivo.write("Línea nueva\n")
#✅ Leer archivo completo:
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#✅ Leer línea por línea:
with open("archivo.txt", "r") as archivo:
    for linea in archivo: #Recorre todo el archivo
        print(linea.strip())

