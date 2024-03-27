import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

df4 = pd.read_csv("Internet_Accesos-por-tecnologia.csv")

def main():
    st.title('Comparación de conexiones en función del año')
    st.sidebar.title('Opciones')
    
    # Filtrar el DataFrame solo para las columnas 'Año', 'Cablemodem', 'ADSL', 'Fibra óptica' y 'Wireless'
    df_selected = df4[['Año', 'Cablemodem', 'ADSL', 'Fibra óptica', 'Wireless']]
    
    # Limpiar los valores en las columnas
    df_selected['Cablemodem'] = df_selected['Cablemodem'].str.replace('.', '').astype(float)
    df_selected['ADSL'] = df_selected['ADSL'].str.replace('.', '').astype(float)
    df_selected['Fibra óptica'] = df_selected['Fibra óptica'].str.replace('.', '').astype(float)
    
    # Agrupar los datos por año y calcular la suma de los valores para cada columna
    df_sum = df_selected.groupby('Año').sum()
    
    # Opciones de visualización
    options = ['Cablemodem', 'ADSL', 'Fibra óptica', 'Wireless']
    selected_options = st.sidebar.multiselect('Seleccione las opciones', options, default=options)
    
    generate_plot = st.button("Generar gráfico")
    
    if generate_plot:
        # Crear el gráfico de líneas para cada opción seleccionada
        for option in selected_options:
            plt.plot(df_sum.index, df_sum[option], marker='o', label=option)
        
        # Etiquetas y título del gráfico
        plt.xlabel('Año')
        plt.ylabel('Cantidad')
        plt.title('Comparación de conexiones en función del año')
        
        # Mostrar leyenda
        plt.legend()
        
        # Mostrar el gráfico
        st.pyplot(plt.gcf())

if __name__ == '__main__':
    main()

