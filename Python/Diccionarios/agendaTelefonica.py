AgendaTelefonica={}

while True:
    Nombre_digitado=input('Digete nombre completo: ')
    if Nombre_digitado=="salir":
        print('Saliendo')
        break
    
    AgendaTelefonica['Nombre']= Nombre_digitado
    AgendaTelefonica['Telefono']=input('Digete telefono: ')

for nombre, telefono in AgendaTelefonica.items():
    print(f"{nombre}: {telefono}")
