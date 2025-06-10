import pandas as pd
# Cargar archivo Excel
archivo = "BD Prueba técnica Support Specialist.xlsx"
df = pd.read_excel(archivo, sheet_name=None)
df_estudiantes = df['BDEstudiantes']
df_eq = df['EQ']
# Filtrar columnas necesarias
notas = df_estudiantes[['ID de usuario', 'Nombre completo', 'Código de oferta de cursos', 'Calificación final rectificada (porcentaje)']]
creditos = df_eq[['ID de usuario', 'Código de oferta de cursos', 'Créditos']]
# Unir por ID y curso
df_comb = pd.merge(notas, creditos, on=['ID de usuario', 'Código de oferta de cursos'], how='left')
df_comb.dropna(subset=['Calificación final rectificada (porcentaje)', 'Créditos'], inplace=True)
# Calcular ponderado
df_comb['ponderado'] = df_comb['Calificación final rectificada (porcentaje)'] * df_comb['Créditos']
# Agrupar por estudiante
resumen = df_comb.groupby(['ID de usuario', 'Nombre completo']).agg(
    total_ponderado=('ponderado', 'sum'),
    total_creditos=('Créditos', 'sum')
).reset_index()
resumen['promedio_ponderado'] = resumen['total_ponderado'] / resumen['total_creditos']
# Calificación literal
def obtener_literal(promedio):
    if promedio < 60: return 'F'
    elif promedio < 70: return 'D'
    elif promedio < 75: return 'C'
    elif promedio < 80: return 'C+'
    elif promedio < 85: return 'B'
    elif promedio < 90: return 'B+'
    elif promedio < 95: return 'A'
    else: return 'A+'
resumen['calificacion_literal'] = resumen['promedio_ponderado'].apply(obtener_literal)
# Separar nombres y apellidos
def separar_nombre_apellido(nombre):
    partes = str(nombre).split()
    if len(partes) >= 4:
        return " ".join(partes[:2]), " ".join(partes[2:])
    elif len(partes) == 3:
        return partes[0], " ".join(partes[1:])
    elif len(partes) == 2:
        return partes[0], partes[1]
    return nombre, ''
resumen[['Nombres', 'Apellidos']] = resumen['Nombre completo'].apply(lambda x: pd.Series(separar_nombre_apellido(x)))
# Exportar resultados
resumen_final = resumen[[
    'ID de usuario', 'Nombre completo', 'Nombres', 'Apellidos',
    'promedio_ponderado', 'total_creditos', 'calificacion_literal'
]]
resumen_final.to_excel("Resultados_Estudiantes.xlsx", index=False)
print("Archivo exportado como 'Resultados_Estudiantes.xlsx'")