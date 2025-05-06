try:
    numero=int(input("Escriba un Numero: "))
    print(10/numero)
except ValueError:
    print("Debes escribir un numero valido: ")
except ZeroDivisionError:
    print("No se puede divir en cero")


