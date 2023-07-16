#import library
import streamlit as st

st.title("Telecomunicaciones Argentina")

st.markdown("***")
st.markdown("## Importancia")

texto_markdown = """
-Las telecomunicaciones permiten la transmisión instantánea y eficiente de información a larga distancia.

-Estas tecnologías son vitales para la conectividad global, facilitando la comunicación entre personas, organizaciones y países en tiempo real.

-Las telecomunicaciones son la base de la infraestructura de Internet, permitiendo el acceso a la información, el comercio electrónico, la educación en línea y la colaboración a nivel mundial.

-Estas tecnologías son fundamentales para el desarrollo económico, al impulsar la innovación, el emprendimiento y la creación de empleo en la industria de las telecomunicaciones.

-Las telecomunicaciones desempeñan un papel crucial en situaciones de emergencia y desastres, permitiendo la coordinación de los esfuerzos de rescate, la comunicación con personas afectadas y la difusión de información importante.

-En comparación con la media mundial, Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, teniendo para el 2020 un total de 62,12 millones de conexiones.
"""

st.markdown(texto_markdown)

st.sidebar.markdown("Analisis de df extraidos de Enacom")


