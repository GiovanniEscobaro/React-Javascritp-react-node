def numeros():
    lista=[]
    while True:
        try:
            DigiteNumero=input('Digete numero(para detener digita salir) : ')
            if DigiteNumero=="salir":
                print("Saliendo")
                break
            elif DigiteNumero.isdigit():
                numero=int(DigiteNumero)
                lista.append(numero)
            else:
                print("Error: La entrada no es un numero")
        except ValueError:
            print("Error: La entrada no es numero entero")
    print(f'Lista de numeros: {lista}')

numeros()

      