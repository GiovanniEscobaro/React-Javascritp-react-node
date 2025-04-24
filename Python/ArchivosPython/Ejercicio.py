#Ejercicio Guarda un mensaje
i=1
while True:
    mensaje=input("Escribe un mensale(0 para salir: ")
    if mensaje=='0':
        print("Saliendo.....")
        break
    with open("mensajes.txt","a") as archivo:
        archivo.write(mensaje + "\n") 
    print(f'el mensaje {i} fue guardado')
    i+=1

with open ("mensajes.txt","r") as archivo:
    for linea in archivo:
        print(linea.strip())   
        

