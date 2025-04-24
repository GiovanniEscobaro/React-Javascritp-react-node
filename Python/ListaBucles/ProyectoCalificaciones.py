calificar=[]
def pedir_calificaciones():
    
    calificaciones=int(input('Digete cantida de calificaciones: '))
    for i in range(calificaciones):
        while True:
            try:
                nota=int(input(f"Ingrese calificación #{i + 1} (0 a 20): "))
                if 0<= nota <= 20:
                    calificar.append(nota)
                    break
                else:
                    print("⚠️ La calificacion debe estar en 0 y 20.")
            except ValueError:
                print('Ingrese un numero valido. ')
    return calificar

def analizar_calificaciones(lista):
    suma=sum(lista)
    mayor=max(lista)
    menor=min(lista)
    promedio=sum(lista)/len(lista)
    return promedio, menor, mayor, suma
def resultados (promedio, menor, mayor,suma):
    print("\n📊 RESULTADOS")
    print(f"- Promedio: {promedio:.2f}")
    print(f"- Nota más alta: {mayor}")
    print(f"- Nota más baja: {menor}")
    print(f"- Suma de notas: {suma}")

print("🎓 ANALIZADOR DE CALIFICACIONES\n")
pedir_calificaciones()
promedio, alta, baja, suma = analizar_calificaciones(calificar)
resultados(promedio, alta, baja,suma)




