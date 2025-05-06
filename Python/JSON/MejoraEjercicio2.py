import json
import os

archivo_json = "personas.json"

# 1. Cargar datos existentes
if os.path.exists(archivo_json):
    with open(archivo_json, "r") as archivo:
        datos = json.load(archivo)
        if isinstance(datos, list):
            personas = datos
        else:
            personas = [datos]
else:
    personas = []

# 2. Mostrar las personas guardadas
if personas:
    print("\n👥 Personas registradas:")
    for i, persona in enumerate(personas, start=1):
        print(f"{i}. {persona['nombre']} | Edad: {persona['edad']} | Correo: {persona['correo']}")
else:
    print("\n🔍 No hay personas registradas aún.")

# 3. Pedir nuevos datos
print("\n🆕 Agrega una nueva persona:")
nombre = input("Nombre: ")
edad = input("Edad: ")
correo = input("Correo: ")

nueva_persona = {
    "nombre": nombre,
    "edad": edad,
    "correo": correo
}

# 4. Agregar y guardar
personas.append(nueva_persona)

with open(archivo_json, "w") as archivo:
    json.dump(personas, archivo, indent=4)

print(f"\n✅ Persona agregada. Total de registros: {len(personas)}")
