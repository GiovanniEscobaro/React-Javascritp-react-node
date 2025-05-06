
import json
import os

archivo_json = "personas.json"
registros_por_pagina = 5  # Cambia esto si quieres ver más o menos por página

# 1. Cargar los datos
if not os.path.exists(archivo_json):
    print("⚠️ El archivo 'personas.json' no existe aún.")
    exit()

with open(archivo_json, "r") as archivo:
    personas = json.load(archivo)
    if not isinstance(personas, list):
        personas = [personas]

total = len(personas)
paginas = (total + registros_por_pagina - 1) // registros_por_pagina  # total de páginas
pagina_actual = 0

# 2. Mostrar por páginas
while True:
    os.system("cls" if os.name == "nt" else "clear")  # Limpia pantalla

    inicio = pagina_actual * registros_por_pagina
    fin = inicio + registros_por_pagina
    subset = personas[inicio:fin]

    print(f"\n📄 Página {pagina_actual + 1} de {paginas}\n")
    for i, persona in enumerate(subset, start=inicio + 1):
        print(f"{i}. {persona['nombre']} | Edad: {persona['edad']} | Correo: {persona['correo']}")

    # 3. Opciones de navegación
    print("\n[N] Siguiente página | [P] Página anterior | [S] Salir")
    opcion = input("👉 Elige una opción: ").strip().lower()

    if opcion == "n" and pagina_actual < paginas - 1:
        pagina_actual += 1
    elif opcion == "p" and pagina_actual > 0:
        pagina_actual -= 1
    elif opcion == "s":
        print("👋 Saliendo del visor.")
        break
    else:
        print("⚠️ Opción no válida.")