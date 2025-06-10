# Crea una función que reciba una cadena y devuelva True si es un palíndromo (se lee igual al derecho y al revés), o False si no lo es.
cadena=input('Digite cadena pae ver si es un palindramo: ')
def palindromo(cadena):
    cadena=cadena.replace(" ","").lower()
    print(cadena)
    return cadena== cadena[::-1]

print(palindromo(cadena))

    
    