import json

# Datos que quieres guardar
datos = {
    "nombre": "Ana",
    "edad": 28,
    "correo": "ana@example.com"
}

# Nombre del archivo
nombre_archivo = "persona.json"

# Crear y guardar el archivo JSON
with open(nombre_archivo, "w") as archivo:
    json.dump(datos, archivo, indent=4)

print("✅ Archivo JSON creado correctamente.")