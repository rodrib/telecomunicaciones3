import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

st.title("Kpi Telecocomunicaciones")

st.markdown("***")
st.markdown("## Importancia")

df1_kpi = pd.read_csv("Acceso a Internet fijo por tecnología y provincia.csv")

if st.checkbox("Mostrar Acceso a Internet fijo por tecnología y provincia"):
    st.dataframe(df1_kpi)

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

#################

#Internet Ingresos

