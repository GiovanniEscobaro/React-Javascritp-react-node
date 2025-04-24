#Listas
frutas=["manzanas","madarinas","peras","banana"]
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
frutas.append("uva")      # añade al final
frutas.remove("peras")     # elimina por valor


#recorido de de una listas
for fruta in frutas:
    print(f"Me gusta {fruta}")


frutas[1]="sandia" #lo puede repalzar asi
print(f'Nueva fruta {frutas[1]}')
            # cantidad de elementos

print(len(frutas))                 #cantida de elementos