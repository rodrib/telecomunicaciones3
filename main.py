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

st.markdown("## Somos Data_So")

texto_markdown1 = """
-Somos una empresa de Data + Soluciones Optimas (SO) = Data_So

-Nos enfoncamos en brindar soluciones a todo tipo de problemas de datos.

-Construimos una respuestas en base a los requerimientos del cliente.

-Y como nos apasiona lo que hacemos, estamos 24/7 para cualquier consulta

-A partir de ahora construyamos esta historia junto, donde analizaremos las oportunidades, ventajas y desventajas.

"""

st.markdown(texto_markdown1)

st.markdown("## Guia")

texto_markdown2 = """
-A la izquierda hay un panel de visualizaciones para interactuar

->Visualizacion1: Acceso a Internet fijo por tecnología y provincia.

->Visualizacion2: Internet_Accesos-por-tecnologia.

->Visualizacion3: Internet_Accesos-por-tecnologia.

->Visualizacion4: Velocidad media de bajada de Internet fijo por provincia.

->Visualizacion5: Denuncias_y_reclamos_202306-1.

->Kpi :

Acceso a Internet fijo por tecnología y provincia
---> Usamos Penetracion de la Fibra Optica

Internet_Ingresos
---> Ingresos Trimestrales

Internet_Penetracion
---> Variaciones Trimestrales y Anuales

Denuncias_y_reclamos_202306-1
---> Total de Reclamos por Mes
"""

st.markdown(texto_markdown2)


st.markdown("# EDA completo")

link_eda = "https://colab.research.google.com/drive/1F8Ol8UTifHitnDf9plV360CIDNuHCOJN?usp=drive_link"

st.markdown(link_eda)

st.sidebar.markdown("Analisis de df extraidos de Enacom")


