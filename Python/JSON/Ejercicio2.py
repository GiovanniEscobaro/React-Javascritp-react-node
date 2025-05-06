import json
import os

# Nombre del archivo
archivo_json = "personas.json"

# 1. Cargar datos existentes
if os.path.exists(archivo_json):
    with open(archivo_json, "r") as archivo:
        personas = json.load(archivo)
else:
    personas = []

# 2. Pedir nuevos datos al usuario
nombre = input("📝 Escribe tu nombre: ")
edad = input("🎂 Escribe tu edad: ")
correo = input("📧 Escribe tu correo: ")

# 3. Crear nuevo registro
nueva_persona = {
    "nombre": nombre,
    "edad": edad,
    "correo": correo
}

# 4. Agregarlo a la lista
personas.append(nueva_persona)

# 5. Guardar todo de nuevo en el archivo
with open(archivo_json, "w") as archivo:
    json.dump(personas, archivo, indent=4)


print(f"✅ Persona agregada correctamente. Total de registros: {len(personas)}")
personas= "personas.json"
print(personas)
