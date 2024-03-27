import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

df9 = pd.read_csv("Velocidad media de bajada de Internet fijo por provincia.csv")

import streamlit as st
import matplotlib.pyplot as plt

# Suponiendo que 'df9' es tu DataFrame
provincias = df9['Provincia']
mbps = df9['Mbps (Media de bajada)']

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño de la figura
ax.bar(provincias, mbps)
ax.set_xlabel('Provincia')
ax.set_ylabel('Mbps')
ax.set_title('Provincia vs Mbps')

# Opcional: Rotar las etiquetas del eje x si hay muchas provincias
ax.tick_params(axis='x', rotation=90)

# Checkbox para mostrar o no el gráfico completo
mostrar_completo = st.checkbox('Mostrar gráfico completo')

# Mostrar el gráfico según el estado del checkbox
if mostrar_completo:
    st.pyplot(fig)
else:
    st.pyplot(plt, bbox_inches='tight')
