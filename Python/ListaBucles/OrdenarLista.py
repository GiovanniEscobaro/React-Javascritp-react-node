#Lista con numeros
NumeroDesorden=[8,7,10,5,1,7,5,6,2,1,4,3,2,9,8,10]
#Variables ascendente y decente
listaOrdenaAsc=[]
listaOrdenasDes=[]
#Lista ordena en mayo a menor y replaza la lista.
NumeroDesorden.sort()
print(f'La lista ordena de menor a mayor {NumeroDesorden}')
#lista ordenada de Menor a Mayor y repalza la lista
NumeroDesorden.sort(reverse=True)

print(f'La lista de odena de mayor a menor {NumeroDesorden}')
lista=[8,7,10,5,1,7,5,6,2,1,4,3,2,9,8,10]
#Se ordena en otra varible 
listaOrdenaAsc=sorted(lista)
print(f'Lista de menor a mayor {listaOrdenaAsc}')
listaOrdenasDes=sorted(lista,reverse=True)
print(f'lista de mayor a menor {listaOrdenasDes}')
print(f'lista original {lista}')


