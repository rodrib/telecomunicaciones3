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


