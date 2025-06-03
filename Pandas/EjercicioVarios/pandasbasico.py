import pandas as pd 

df=pd.read_csv('F:/SoftwareEstudio/Pandas/EjercicioVarios/datos.csv') #Cargar en la archivo a un variable
print(df.head()) 
print(f'{df.columns},  Para mostrar columnas') 
print(f'# Tipos de campos , {df.dtypes}') 
print(df.describe())# Un resume de archvivo
print(df['edad']) # Para mirar cualquie columna
print(df[['edad','nombre']])# Para mirar dos o mas columnas
print(df.iloc[0,3])# Para mirar la colunma por numero
print(df.loc[2,'id'])# Acuerdes todas la columnas empizas de desde cero
print(df[df['edad']>10])# Edad mayores a 10.
print(df.dropna())# Borra todas todos los registro que tiene un campo nul
print(df.fillna('0'))#y rezplaza todos los campon null por 0
print(df.groupby('id').sum()) # Suma
print(df.groupby('id').count())# Cuenta
df.to_csv('nuevo_datos.csv',index=False)
df.rename(columns={'sex','genero'},inplace=True) # para renombrar un columna

#leer varios archivos pd.read*/*/ u sectencia de sql
archivo_csv=pd.read_csv('F:/SoftwareEstudio/Pandas/Particas/archivos.csv')
print(archivo_csv)
archivo_exel=pd.read_excel('F:/SoftwareEstudio/Pandas/Particas/Movimientoventasminicargador2024.xlsx')
print(archivo_exel)



