import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

df10 = pd.read_csv("Denuncias_y_reclamos_202306-1.csv")

import streamlit as st
import matplotlib.pyplot as plt

def mostrar_grafico():
    # Agrupar por operador y motivo de reclamo, y calcular la suma de la cantidad
    agrupado = df10.groupby(['Operador', 'Motivo de Reclamo'])['Cantidad'].sum().reset_index()

    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(10, 6))

    # Obtener los dos mayores operadores por cantidad
    mayores_operadores = agrupado.groupby('Operador')['Cantidad'].sum().nlargest(2).index

    # Definir colores personalizados para los dos mayores operadores
    colores = {
        mayores_operadores[0]: '#1f77b4',  # Azul
        mayores_operadores[1]: '#ff7f0e',  # Naranja
    }

    # Iterar sobre cada operador para crear las barras correspondientes
    for i, operador in enumerate(agrupado['Operador'].unique()):
        datos_operador = agrupado[agrupado['Operador'] == operador]

        # Obtener el color correspondiente al operador
        color = colores.get(operador, 'gray')

        ax.bar(datos_operador['Motivo de Reclamo'], datos_operador['Cantidad'], label=operador, color=color)

        # Agregar etiquetas encima de las barras de los dos mayores operadores
        if operador in mayores_operadores:
            for j, cantidad in enumerate(datos_operador['Cantidad']):
                ax.text(j, cantidad, str(cantidad), ha='center', va='bottom')

    # Añadir etiquetas y título al gráfico
    ax.set_xlabel('Motivo de Reclamo')
    ax.set_ylabel('Cantidad')
    ax.set_title('Motivo de Reclamo y Cantidad por Operador')
    ax.legend()

    # Ajustar el espaciado de los ejes x
    plt.xticks(rotation=90)

    # Mostrar el gráfico
    st.pyplot(fig)

if st.checkbox('Mostrar gráfico'):
    mostrar_grafico()

