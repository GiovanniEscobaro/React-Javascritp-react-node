grande = {}
for i in range(1_000_000):
    grande[f"clave{i}"] = i

print("Diccionario con 1 millón de registros creado.")
contador=0
for clave, valor in grande.items():
    print(f"{clave}: {valor}")
    contador += 1
    if contador == 100:  # Cambia este número si quieres más o menos
        break