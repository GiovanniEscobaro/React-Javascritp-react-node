def tarea():
    tareas=[]
    while True:
        digitetareas=input('Digita la tarea para cargar(para terminar digata salir): ')
        if digitetareas=="salir":
            break
        else:
            tareas.append(digitetareas)

    print(f'la tareas son: {tareas}')
tarea()
