#import library
import streamlit as st

import pandas as pd

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