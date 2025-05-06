import json
import os

ARCHIVO_JSON = "agenda.json"

def cargar_contactos():
    if not os.path.exists(ARCHIVO_JSON):
        return []
    with open(ARCHIVO_JSON, "r") as archivo:
        return json.load(archivo)

def guardar_contactos(contactos):
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(contactos, archivo, indent=4)

def mostrar_menu():
    print("\n📱 AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto por nombre")
    print("4. Eliminar contacto")
    print("5. Salir")

def agregar_contacto(contactos):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
    contactos.append(contacto)
    guardar_contactos(contactos)
    print("✅ Contacto guardado.")

def ver_contactos(contactos):
    if not contactos:
        print("📭 No hay contactos guardados.")
        return
    print("\n📋 Lista de contactos:")
    for idx, c in enumerate(contactos, 1):
        print(f"{idx}. {c['nombre']} | Tel: {c['telefono']} | Email: {c['correo']}")

def buscar_contacto(contactos):
    nombre = input("🔍 Buscar nombre: ").lower()
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre]
    
    if encontrados:
        for c in encontrados:
            print(f"✔️ {c['nombre']} | Tel: {c['telefono']} | Email: {c['correo']}")
    else:
        print("❌ No se encontró ese contacto.")

def eliminar_contacto(contactos):
    nombre = input("🗑️ Nombre del contacto a eliminar: ").lower()
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre]

    if not encontrados:
        print("❌ No se encontró ese contacto.")
        return

    for contacto in encontrados:
        print(f"¿Eliminar a {contacto['nombre']} (Tel: {contacto['telefono']})?")
        confirmacion = input("Escribe 'sí' para confirmar: ").lower()
        if confirmacion == "sí":
            contactos.remove(contacto)
            print("✅ Contacto eliminado.")
            guardar_contactos(contactos)

# --- Programa principal ---
agenda = cargar_contactos()

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        ver_contactos(agenda)
    elif opcion == "3":
        buscar_contacto(agenda)
    elif opcion == "4":
        eliminar_contacto(agenda)
    elif opcion == "5":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción inválida.")
