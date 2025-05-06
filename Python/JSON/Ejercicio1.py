import json
nombre=input("Escriba su nombre: ")
edad=input("Escriba tu edad: ")
correo=input ("Escribe tu correo: ")

persona= {
    "nombre": nombre,
    "edad": edad,
    "correo": correo
}
# 3. Guardamos en un archivo JSON

with open("usuario.json","w") as archivo:
    json.dump(persona,archivo,indent=4)

print(" Tus datos ha sido guarda en usuario.json")