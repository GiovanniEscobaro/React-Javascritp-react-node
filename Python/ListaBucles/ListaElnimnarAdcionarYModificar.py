#Lista con 3 frutas
frutas=["Manzana", "Pera", "Banado"]
#Impreme la frutas de la pociosion 0
print(frutas[0])
print("Original: ", frutas)
#Adcionar una fruta en un lista
frutas.append("Piña")
#Remover un fruta
frutas.remove("Manzana")
#Imprimir todas los frutas
for fruta in frutas:
    print(fruta)
# cambia un fruta
contador=0
for fruta in frutas:
    if fruta== "Pera":
        frutas[contador]="Patilla"
    contador+=1
print(f'El cambio quedo asi {frutas}')




