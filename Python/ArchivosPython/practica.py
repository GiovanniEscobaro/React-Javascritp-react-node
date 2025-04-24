ARCHIVO_CONTACTOS = "agenda.txt"

def cargar_contactos():
    contactos = []
    try:
        with open(ARCHIVO_CONTACTOS, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nombre, telefono, correo = partes
                    contactos.append({
                        "nombre": nombre,
                        "telefono": telefono,
                        "correo": correo
                    })
    except FileNotFoundError:
        pass  # Si el archivo no existe aún, empezamos con lista vacía
    return contactos

def guardar_contacto(contacto):
    with open(ARCHIVO_CONTACTOS, "a") as archivo:
        archivo.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['correo']}\n")

def mostrar_menu():
    print("\n📱 AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto por nombre")
    print("4. Salir")

def agregar_contacto(contactos):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
    contactos.append(contacto)
    guardar_contacto(contacto)
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

# --- Programa principal ---
agenda = cargar_contactos()

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        ver_contactos(agenda)
    elif opcion == "3":
        buscar_contacto(agenda)
    elif opcion == "4":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción inválida.")

        
