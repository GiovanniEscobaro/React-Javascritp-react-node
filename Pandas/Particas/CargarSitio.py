import pandas as pd

# Se asignan una variable 
Panarchivo=pd.read_csv('F:/SoftwareEstudio/Pandas/Particas/archivos.csv')

# Y se imprime los primero 10
print(Panarchivo.head(10))
print(f'Numero 10 {Panarchivo.columns[10]}')
print(f'Numero de filas y columnas :',Panarchivo.shape)
print(f'Tipo de datos csv: ', Panarchivo.info())
print(f' Estadista: ', Panarchivo.describe()) 
print(f' pasageros del titane por survived ', Panarchivo.groupby('survived').count())
print(f' pasageros del titane ', len(Panarchivo))
promedio_edad=Panarchivo['age'].mean()
print(f'Promedio de edad', promedio_edad)
print(f'Columnas son: , {len(Panarchivo.columns)} columnas')
print(f'Numero de filas son: {len(Panarchivo)} filas')

# Muestre todas las edades, Muestre solo los Sexo y edades, muestre
# los pasajeros mayores de 60 años
print(f'Todas la edadas solmente ', Panarchivo['age'])
print(f'Sexo y Edades ', Panarchivo[['sex','age']] )
print(f'Mayores a 60 años: ', Panarchivo[Panarchivo['age']>60])

# Que columnas tienes nulo, Rellene los nulos de la colunma con 0
# Renombre columna sex por genero
# Que columnas tienes nulo
nulos_por_columna=Panarchivo.isnull().sum()
#Es el conteo de el total de columnas que tenga null

# Que columnas tienes nulo, Rellene los nulos de la colunma con 0
print(f'Cuenta el Valor Nulo de todas la columnas: {nulos_por_columna}')
#Se filta por los que si tiene valor nulo.
colunma_con_nulos=nulos_por_columna[nulos_por_columna>0]
print(f'Columnas con valures nulos: {colunma_con_nulos}')
print(Panarchivo.fillna(0))
# Renombre columna sex por genero
Panarchivo.rename(columns={'sex':'genero'},inplace=True) 
print(f'Se verifica si camnio sex por genero {Panarchivo.columns}')
