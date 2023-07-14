#import library
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df4 = pd.read_csv("Internet_Accesos-por-tecnologia.csv")

if st.checkbox("Mostrar Acceso a Internet por tecnología"):
    st.dataframe(df4)

if st.checkbox("Vista de los datos Head o Tail"):
    if st.button("Head"):
        st.write(df4.head())
    if st.button("Tail"):
        st.write(df4.tail())

dim = st.radio("Dimension a Mostrar:",("Filas","Columnas"))

if dim == "Filas":
    st.write("Cantidad de filas ", df4.shape[0])
else:
    st.write("Cantidad de columnas ", df4.shape[1])


import streamlit as st
import matplotlib.pyplot as plt

import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title('Generador de gráficos de Cablemodem')
    
    # Filtrar el DataFrame solo para la columna 'Año' y 'Cablemodem'
    df_cablemodem = df4[['Año', 'Cablemodem']]
    
    start_year = st.slider("Año inicial", min_value=int(df_cablemodem['Año'].min()), max_value=int(df_cablemodem['Año'].max()), value=int(df_cablemodem['Año'].min()))
    end_year = st.slider("Año final", min_value=int(start_year), max_value=int(df_cablemodem['Año'].max()), value=int(df_cablemodem['Año'].max()))
    generate_plot = st.checkbox("Generar gráfico")
    
    if generate_plot:
        # Agrupar los datos por año y calcular la suma de los valores de Cablemodem para cada año
        df_filtered = df_cablemodem[(df_cablemodem['Año'] >= start_year) & (df_cablemodem['Año'] <= end_year)]
        df_filtered_sum = df_filtered.groupby('Año').sum()
        
        # Crear el gráfico de líneas
        plt.plot(df_filtered_sum.index, df_filtered_sum['Cablemodem'], marker='o')
        plt.xlabel('Año')
        plt.ylabel('Cablemodem')
        plt.title('Cablemodem en función del Año')
        
        # Mostrar el gráfico
        st.pyplot(plt.gcf())

if __name__ == '__main__':
    main()
