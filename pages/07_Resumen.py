import streamlit as st

st.title("Telecomunicaciones Argentina")

st.markdown("***")
st.markdown("## Resumen")

texto_resumen = """
Existen diferencias en la distribución de tecnologías entre provincias. Por ejemplo, en Chaco hay pocos servicios "Otros", mientras que en Formosa hay una diferencia significativa en comparación con Chaco. En Buenos Aires vs La Pampa, esta última tiene una gran cantidad de "cablemódem", mientras que en Provincia de Buenos Aires es casi inexistente.

El servicio de fibra óptica fue el que más creció trimestre a trimestre. Las provincias de la región de la Patagonia (Río Negro, Santa Cruz y Tierra del Fuego) tienen los valores más altos de fibra óptica.

Se realizaron agrupamientos por regiones, y se encontró que el servicio que más creció en el NEA fue la fibra óptica, mientras que en el NOA fue el inalámbrico. Además, las provincias pertenecientes a una misma región también son heterogéneas en cuanto a los tipos de servicio.

En cuanto a los accesos a internet fijo por tecnología y localidad, se encontró que todas las capitales tienen tipos de servicios diferentes entre sí. Esto puede ser un punto de partida para agregar servicios a las localidades cercanas en lugar de comenzar desde cero.

Se analizó el acceso a internet fijo por velocidad de bajada y localidad, centrándose en la provincia de Formosa como ejemplo. Se encontró que todos los departamentos de la provincia tienen áreas con velocidades de megabits por segundo (mbps) bajas. Sin embargo, esto puede deberse a que, aunque algunas localidades tengan un buen acceso a internet, no todas las áreas del departamento están cubiertas.

En relación con los tipos de tecnología de acceso a internet, se observó que el servicio inalámbrico se mantiene constante, pero el ADSL ha disminuido a lo largo de los años. El cablemódem y la fibra óptica han experimentado aumentos, pero recientemente el cablemódem ha disminuido. Se plantea la hipótesis de que esto puede estar relacionado con el aumento de la fibra óptica, aunque se necesitan pruebas estadísticas para confirmar esta idea.

Se encontró que la Ciudad de Buenos Aires y Córdoba son las que tienen menor banda ancha fija. Esto podría deberse a que son provincias grandes y heterogéneas en términos de ciudades.

Se observó que los trimestres con mayores ingresos en el periodo de 2014 a 2022 son abril-junio y julio-septiembre.

En cuanto a la penetración de internet, la Ciudad de Buenos Aires es el distrito con el mayor número, lo cual es esperado debido a que es la capital de Argentina y alberga muchas empresas y tecnologías. Santiago del Estero es la provincia con menor acceso a internet por cada 100 hogares, lo cual podría ser resultado de varios factores como hogares sin necesidades satisfechas, políticas centralizadas o pueblos pequeños y dispersos.

En relación con las denuncias y reclamos, se encontró que Telecom y Telefónica son los operadores con más reclamos, principalmente por problemas técnicos. Esto es importante tenerlo en cuenta para brindar servicios de buena calidad. Además, se destaca que dos empresas concentran la mayor parte de los reclamos y denuncias, incluyendo nuevamente a Telefónica, que también presentaba problemas técnicos en el análisis anterior.
"""

st.markdown(texto_resumen)