def divirdir_100():
    try:
        number=int(input('Ingreser Numero: '))
        result=100 / number
        print(f'El numero divido en 100 es: {result}')
    except ValueError as e:
       print('No debes ingresa un texto')
    except ZeroDivisionError as e:
        print('No se pude dividir entre 0')
divirdir_100()
