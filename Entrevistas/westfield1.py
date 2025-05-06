if canal == "feria" and idioma == "inglés":
    propietario = "Propietario 4"
elif pais == "EE.UU." and tipo_cliente == "B2B":
    propietario = "Propietario 1"
elif pais == "Colombia" and tipo_cliente == "B2C":
    propietario = "Propietario 2"
elif canal == "orgánico":
    propietario = "Propietario 3"
elif canal == "pagado" or canal == "referido":
    propietario = "Propietario 4"
else:
    propietario = "Propietario 3"  # Asignación por defecto