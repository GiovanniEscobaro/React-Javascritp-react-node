def show_number():
    try:
        number= int(input('Ingeres un numero entero: '))
        print(f' El numero entero es: {number}')
    #except Exception as e:
     #   print(type(e))
    except ValueError as e:
        print('He ingreso un texto solo numeros')
    except NameError as e:
        print('errro en valiable')
    else:
        print('No se encontro ningu error')
    finally:
        print('Sentenecia final de la ejecucion')
show_number()