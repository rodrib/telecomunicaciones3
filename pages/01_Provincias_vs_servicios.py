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
provincias_seleccionadas = st.multiselect('Selecciona las provincias a comparar', provincias)

if len(provincias_seleccionadas) > 1:
    # Filtrar el DataFrame por las provincias seleccionadas
    df_provincias = df1[df1['Provincia'].isin(provincias_seleccionadas)]

    # Obtener los valores para las categorías de conexión
    valores_provincias = df_provincias[['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']].values

    # Configurar los índices y el ancho de las barras
    indices = np.arange(len(valores_provincias[0]))
    ancho_barra = 0.35

    # Crear el gráfico de barras comparativo
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, provincia in enumerate(provincias_seleccionadas):
        ax.bar(indices + i * ancho_barra, valores_provincias[i], ancho_barra, label=provincia)

    # Configurar las etiquetas de los ejes y el título
    ax.set_xlabel('Tipo')
    ax.set_ylabel('Cantidad')
    ax.set_title('Comparación de conexiones por tipo entre provincias')
    ax.set_xticks(indices + (len(provincias_seleccionadas) - 1) * ancho_barra / 2)
    ax.set_xticklabels(['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros'])
    ax.legend()

    # Ajustar el espacio entre los subplots para evitar solapamiento
    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
else:
    st.warning('Selecciona al menos 2 provincias para comparar')


########

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Suponiendo que ya tienes el DataFrame df1

# Seleccionar las columnas relevantes
columnas = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']

# Convertir las columnas a valores numéricos
df1[columnas] = df1[columnas].apply(pd.to_numeric, errors='coerce')

# Obtener los valores de Trimestre con los valores modificados
trimestres = ['3', '2', '1', '4', '3 *', '2 *', '1 *']

# Calcular los totales por Trimestre para cada columna
totales_por_trimestre = df1.groupby('Trimestre')[columnas].sum()

# Configurar los datos para el gráfico de barras
datos = totales_por_trimestre.reindex(trimestres).values.T

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 8))
ancho_barras = 0.15

for i, columna in enumerate(columnas):
    posiciones_x = range(len(trimestres))
    posiciones_x_desplazadas = [x + i * ancho_barras for x in posiciones_x]
    ax.bar(posiciones_x_desplazadas, datos[i], width=ancho_barras, label=columna)

# Configurar las etiquetas de los ejes y el título
ax.set_xlabel('Trimestre')
ax.set_ylabel('Valores')
ax.set_title('Valores por Trimestre y Columna')

# Ajustar las etiquetas del eje x con rotación de 45 grados
ax.set_xticks(posiciones_x)
ax.set_xticklabels(trimestres, rotation=45)

# Ajustar la leyenda
ax.legend(title='Columna')

# Mostrar el gráfico
if st.checkbox('Mostrar gráfico Valores por Trimestre'):
    st.pyplot(fig)



#####################

# uso de slidebar en Trimestre

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Suponiendo que ya tienes el DataFrame df1

# Definir los trimestres específicos
trimestres = ['3', '2', '1', '4', '3 *', '2 *', '1 *']

# Crear un selectbox para elegir el servicio
servicio = st.selectbox('Selecciona un servicio', ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros'])

# Mostrar el slider para seleccionar el trimestre
trimestre_seleccionado = st.slider('Selecciona un trimestre', min_value=0, max_value=len(trimestres)-1, step=1)

# Obtener el valor de trimestre correspondiente a la selección
trimestre = trimestres[trimestre_seleccionado]

# Filtrar el DataFrame por el servicio y trimestre seleccionado
df_filtrado = df1[(df1['Trimestre'] == trimestre)]

# Obtener los valores del servicio seleccionado
valores = df_filtrado[servicio]

# Crear el gráfico de barras
fig, ax = plt.subplots()
ax.bar(df_filtrado['Trimestre'], valores, width=0.2)  # Modificar el ancho de las barras aquí

# Configurar las etiquetas de los ejes y el título
ax.set_xlabel('Trimestre')
ax.set_ylabel('Valores')
ax.set_title(f'Valores de {servicio} por Trimestre')

# Mostrar el gráfico
st.pyplot(fig)







