import pandas as pd
datos={
    'Nombre': ['Ana', 'Luis','Giovannni'],
    'Edad': [23,36,29],
    'Ciudad':['Cali', 'Bogota', 'Santa Marta']

}
df=pd.DataFrame(datos)
# Adicionar un valor salario
salario= [1000,2000,1500]
df['Salario']=salario

#Modifificar un campo
df.at[1,'Ciudad']='Nilo'

print(df)
#Leer archivo
archivo_csv=pd.read_csv('F:/SoftwareEstudio/Pandas/Particas/archivos.csv')
print(archivo_csv)
#leer lo primero 10 regitros
print(archivo_csv.head(10))
#Muestra informacio del archivo colunma y filas
print(archivo_csv.info)

#Filtro para mostra el age mayor a 50 
archivo_csv_filtro=archivo_csv[archivo_csv['age']>50 ]
print(archivo_csv_filtro)
#Se filtra por sex male
archivo_csv_filtro=archivo_csv[(archivo_csv['sex']=='male')& (archivo_csv['sibsp']==0)]
print(archivo_csv_filtro)




