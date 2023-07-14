#import library
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Acceso a Intertet fijo por tecnologia y provincia
df1 = pd.read_csv("Acceso a Internet fijo por tecnología y provincia.csv")

if st.checkbox("Mostrar Acceso a Internet fijo por tecnología y provincia"):
    st.dataframe(df1)

if st.checkbox("Vista de los datos Head o Tail"):
    if st.button("Head"):
        st.write(df1.head())
    if st.button("Tail"):
        st.write(df1.tail())

dim = st.radio("Dimension a Mostrar:",("Filas","Columnas"))

if dim == "Filas":
    st.write("Cantidad de filas ", df1.shape[0])
else:
    st.write("Cantidad de columnas ", df1.shape[1])



## Tecnologia por Provincia

#Codigo de Porcentaje de Tecnologia por Provincia

# Seleccionar las columnas relevantes
columnas = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']


# Convertir las columnas a valores numéricos
df1[columnas] = df1[columnas].apply(pd.to_numeric, errors='coerce')

# Obtener los valores agregados por tipo de conexión y provincia
df_agg = df1.groupby('Provincia')[columnas].sum()

# Calcular los porcentajes para cada tipo de conexión en cada provincia
porcentajes = df_agg.div(df_agg.sum(axis=1), axis=0) * 100

# Obtener las provincias y los porcentajes
provincias = porcentajes.index.tolist()
datos = porcentajes.values.T

# Crear el gráfico de barras apilado
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(provincias, datos[0])

for i in range(1, len(columnas)):
    ax.bar(provincias, datos[i], bottom=sum(datos[:i]))

# Configurar las etiquetas de los ejes y el título
ax.set_xlabel('Provincia')
ax.set_ylabel('Porcentaje')
ax.set_title('Distribución de conexiones por tipo y provincia')

# Configurar la leyenda y ajustar su posición
leg = ax.legend(columnas, title='Tipo', bbox_to_anchor=(1, 1), loc='upper left')

# Rotar los nombres de las columnas en el eje x
plt.xticks(rotation=90)

# Ajustar el espacio entre los subplots para evitar solapamiento
plt.tight_layout()



if st.checkbox("Porcentaje de Tecnologia por Provincia"):
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Obtener las provincias únicas
provincias = df1['Provincia'].unique()

# Mostrar la selección de provincias en Streamlit
provincia_seleccionada1 = st.selectbox('Selecciona la primera provincia', provincias)
provincia_seleccionada2 = st.selectbox('Selecciona la segunda provincia', provincias)

# Filtrar el DataFrame por las provincias seleccionadas
df_provincia1 = df1[df1['Provincia'] == provincia_seleccionada1]
df_provincia2 = df1[df1['Provincia'] == provincia_seleccionada2]

# Obtener los valores para las categorías de conexión
valores_provincia1 = df_provincia1[['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']].values[0]
valores_provincia2 = df_provincia2[['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']].values[0]

# Configurar los índices y el ancho de las barras
indices = np.arange(len(valores_provincia1))
ancho_barra = 0.35

# Crear el gráfico de barras comparativo
fig, ax = plt.subplots(figsize=(10, 8))
bar1 = ax.bar(indices, valores_provincia1, ancho_barra, label=provincia_seleccionada1)
bar2 = ax.bar(indices + ancho_barra, valores_provincia2, ancho_barra, label=provincia_seleccionada2)

# Configurar las etiquetas de los ejes y el título
ax.set_xlabel('Tipo')
ax.set_ylabel('Cantidad')
ax.set_title('Comparación de conexiones por tipo entre provincias')
ax.set_xticks(indices + ancho_barra / 2)
ax.set_xticklabels(['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros'])
ax.legend()

# Ajustar el espacio entre los subplots para evitar solapamiento
plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)