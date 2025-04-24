persona={
    "nombre": "Ana",
    "edad":28,
    "Ciudad":"Cali"
}
print(persona["nombre"])  # Ana
print(persona.get("edad"))  # 28
print(persona.get("Ciudad"))  # Cali
print(persona)

persona["email"] = "ana@email.com"  # nuevo dato
persona["edad"] = 29  # modificar
print(persona.get("email"))
print(persona)
for clave, valor in persona.items():
    print(clave, ":", valor)