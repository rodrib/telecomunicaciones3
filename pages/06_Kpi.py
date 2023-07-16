import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

st.title("Kpi Telecocomunicaciones")

st.markdown("***")
st.markdown("## Importancia")

text1 = """son métricas que se utilizan para medir el desempeño y el progreso de una organización, departamento o proyecto en relación con los objetivos establecidos. Estos indicadores son fundamentales 
porque desempeñan un papel crucial en el éxito y la eficiencia de una entidad.
"""

st.markdown(text1)

df1_kpi = pd.read_csv("Acceso a Internet fijo por tecnología y provincia.csv")

if st.checkbox("Mostrar Acceso a Internet fijo por tecnología y provincia"):
    st.dataframe(df1_kpi)


st.markdown("### Penetracion de la Fibra Optica")

text2 = """Este KPI te permite evaluar la proporción de 
conexiones de fibra óptica en comparación con el total de conexiones. 
"""

st.markdown(text2)
###########

import altair as alt

# Eliminar los puntos de los valores en la columna 'Fibra óptica'
df1_kpi['Fibra óptica'] = df1_kpi['Fibra óptica'].str.replace('.', '')

# Rellenar los valores faltantes con ceros
df1_kpi['Fibra óptica'] = df1_kpi['Fibra óptica'].fillna('0')

# Convertir los valores de la columna 'Fibra óptica' a números enteros
df1_kpi['Fibra óptica'] = pd.to_numeric(df1_kpi['Fibra óptica'], errors='coerce')

# Convertir los valores de la columna 'Total' a números enteros
df1_kpi['Total'] = pd.to_numeric(df1_kpi['Total'], errors='coerce')

# Filtrar las filas correspondientes a la fibra óptica
df_fibra = df1_kpi[df1_kpi['Fibra óptica'] > 0]

# Calcular la penetración de fibra óptica como un porcentaje utilizando la columna 'Total'
penetracion_fibra = (df_fibra['Fibra óptica'] / df_fibra['Total']) * 100

# Ordenar los datos de penetración de fibra óptica de menor a mayor
penetracion_fibra = penetracion_fibra.sort_values(ascending=True)

# Obtener los períodos para el eje X en orden ascendente
periodos = df_fibra['Año'].astype(str) + 'T' + df_fibra['Trimestre'].astype(str)
periodos = periodos.sort_values(ascending=True)

# Crear un DataFrame con los datos
data = pd.DataFrame({"Periodo": periodos, "Penetración de Fibra Óptica (%)": penetracion_fibra})

# Configurar la aplicación de Streamlit
st.title("Penetración de Fibra Óptica")
st.altair_chart(alt.Chart(data).mark_line().encode(
    x="Periodo",
    y="Penetración de Fibra Óptica (%)",
    tooltip=["Periodo", "Penetración de Fibra Óptica (%)"]
).interactive())


text3 = """-Obsservamos que el crecimiento de la fibra optica entre 2014 y 2018 ha sido poco, solo un 20%

-A partir de finales del 2018 y todo el 2019 tenemos una gran disminucion sin embargo en el dataset se menciona
que estos datos no coinciden a Nivel Nacional por lo que deben tomarse con cuidado.

-En 2020 y 2021 tenemos un gran aumento muy posiblemente debido a la necesidad de estar conectados debido a la Pandemia y sus restricciones
"""

st.markdown(text3)

#################

#Internet Ingresos

st.markdown("### Ingresos Trimestrales")

df6_kpi = pd.read_csv("Internet_Ingresos.csv")


# Paso 1: Calcular la suma de ingresos por trimestre
ingresos_trimestrales = df6_kpi.groupby(['Año', 'Trimestre'])['Ingresos (miles de pesos)'].sum()

# Paso 2: Crear una tabla con los resultados
tabla_resultados = pd.DataFrame(ingresos_trimestrales)
tabla_resultados.columns = ['Ingresos Trimestrales']

# Configurar la aplicación de Streamlit
st.title("Ingresos Trimestrales")
st.table(tabla_resultados)

text4 = """
-Vemos que hay un aumento de los ingresos progesivamente con el tiempo, aunque este ingreso comprende la suma de todas las tecnologias.
Esto es algo alentador ya que la tendencia esta en alza y puede ser una buena oportunidad de seguir invirtiendo en tecnologia.
"""

st.markdown(text4)

###################

st.markdown("### Variaciones Trimestrales y Anuales")

df7_kpi = pd.read_csv("Internet_Penetracion.csv")


import streamlit as st
import pandas as pd

# Ordenar el DataFrame por año y trimestre de forma ascendente
df7_kpi.sort_values(by=['Año', 'Trimestre'], inplace=True)

# Convertir la columna 'Accesos por cada 100 hogares' a tipo numérico
df7_kpi['Accesos por cada 100 hogares'] = pd.to_numeric(df7_kpi['Accesos por cada 100 hogares'], errors='coerce')

# Calcular la variación trimestral de Accesos por cada 100 hogares
df7_kpi['Variación Trimestral'] = df7_kpi['Accesos por cada 100 hogares'].pct_change()

# Calcular la variación anual de Accesos por cada 100 hogares
df7_kpi['Variación Anual'] = df7_kpi.groupby('Año')['Accesos por cada 100 hogares'].pct_change(periods=4)

# Mostrar los resultados en Streamlit
st.dataframe(df7_kpi[['Año', 'Trimestre', 'Provincia', 'Variación Trimestral', 'Variación Anual']])

text5 = """
-En esta caso contamos con Variaciones las cuales en algunos casos datos no tenemos un valor.

-En otras con contamos con variaciones Negativas, como en el caso de Santiago del Estero en el 4 Trimestre del 2015,o Neuquen y Santa Cruz
con el Trimestre 4 y periodo 2020. Esto nos puede servir para ver que hechos historicos ocurrieron y tratar de profundizar el porque de esos
retrocesos.

-Cabe mencionar que hay variaciones positivas como Buenos Aires en el periodo 2021-Trimestre 2. Aqui tambien lo mismo ver que implementaciones se pudieron
haber hecho para tenerlas en cuenta el dia de mañana.
"""

st.markdown(text5)
###############

st.markdown("### Total de Reclamos por Mes")

text6 = """Este KPI se utiliza para medir la cantidad de reclamos recibidos por una organización en un período mensual específico.
 Los reclamos pueden ser de diferentes tipos, como reclamos de clientes, reclamos de empleados o reclamos de proveedores. 
"""

st.markdown(text6)

df10_kpi = pd.read_csv("Denuncias_y_reclamos_202306-1.csv")

# Calcular el total de reclamos por mes
total_reclamos_por_mes = df10_kpi.groupby('Mes')['Cantidad'].sum()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
total_reclamos_por_mes.plot(kind='bar', ax=ax)
ax.set_xlabel('Mes')
ax.set_ylabel('Total de Reclamos')
ax.set_title('Total de Reclamos por Mes')
ax.grid(True)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

text7 = """Aqui vemos que los mese mas criticos son el primero y el tercero por lo que nuestras politicas,
tendrian que estar puestas a mejorar los servicios en esos meses.
"""

st.markdown(text7)