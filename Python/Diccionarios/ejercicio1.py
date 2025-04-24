estudiante={}
estudiante['Nombre']=input('Nombre de estudiante: ')
estudiante["edad"]=int(input('Edad: '))
estudiante["curso"]=input('Curso: ')
print('\n \U0001F4CB DATOS DE ESTUDIANTE: ')
for clave,valor in estudiante.items():
    print(f'{clave.capitalize()}: {valor}')

