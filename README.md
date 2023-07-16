# telecomunicaciones3

Telecomunicaciones Argentina

# Importancia
-Las telecomunicaciones permiten la transmisión instantánea y eficiente de información a larga distancia.

-Estas tecnologías son vitales para la conectividad global, facilitando la comunicación entre personas, organizaciones y países en tiempo real.

-Las telecomunicaciones son la base de la infraestructura de Internet, permitiendo el acceso a la información, el comercio electrónico, la educación en línea y la colaboración a nivel mundial.

-Estas tecnologías son fundamentales para el desarrollo económico, al impulsar la innovación, el emprendimiento y la creación de empleo en la industria de las telecomunicaciones.

-Las telecomunicaciones desempeñan un papel crucial en situaciones de emergencia y desastres, permitiendo la coordinación de los esfuerzos de rescate, la comunicación con personas afectadas y la difusión de información importante.

-En comparación con la media mundial, Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, teniendo para el 2020 un total de 62,12 millones de conexiones.

# Somos Data_So
-Somos una empresa de Data + Soluciones Optimas (SO) = Data_So

-Nos enfoncamos en brindar soluciones a todo tipo de problemas de datos.

-Construimos una respuestas en base a los requerimientos del cliente.

-Y como nos apasiona lo que hacemos, estamos 24/7 para cualquier consulta

-A partir de ahora construyamos esta historia junto, donde analizaremos las oportunidades, ventajas y desventajas.

# Link del Dashboard
https://mainpy-eulh7d1l62m.streamlit.app/



# Dataset usados en el EDA

enacom_csv
https://drive.google.com/drive/folders/1vt41JpWVrSVZJdUsI82DcLOVw9y1zoVH?usp=drive_link

De los 16 que habian fueron elegidos 9, se priorizo aquellos que contengan Informacion relevante como: Tipo de Tecnologia, Provincias, Ingresos, Velocidad de Bajada, Tiempo tanto en año como en Trimestre

enacom_cmp_csv
https://drive.google.com/drive/folders/122_cY4EOvt3aYjUuMunYab6RqILXCjL9?usp=drive_link

Estos dataset fueron ya que es complementar o saber cuales son las denuncias y fallas tecnicos en los servicios ofrecidos

# Resultado de los Analisis

Link del EDA
https://colab.research.google.com/drive/1F8Ol8UTifHitnDf9plV360CIDNuHCOJN?usp=sharing

-El enfoque mencionado fue conocer primero los tipos de tecnologia por Provincias:
(Se uso el df1)
-Las Provincias presentena una distribucion diferente en cuanto a los tipos de tecnologia.
-Provincia que en teoria son similares geograficamente presentan una gran diferencia como por ejemplo: Chaco y Formosa donde en Chaco casi no hay muchos servicios correspondientes a "Otros".
-Otro ejemplo se da en Buenos Aires vs La Pampa, en donde esta ultima tiene una gran cantidad en lo que se refiere a "cablemodem" y Provincia de Buenos Aires casi inexistente

En cuanto a los tipos:
-Fibra optica fue el servicio que mas crecio por Trimestre
-Los valores mas altos de fibra optica son de las Provincias de la region de la Patagonia: Rio Negro , Santa Cruz y Tierra del Fuego

Tambien se realizo un agrupamiento por Regiones:
-El servicio que mas crecio en el Nea fue fibra optica
-En el Noa wirelles
-Provincias que pertenecen a una misma region tambien son heterogeneas en cuanto a los tipos de servicio

Accesos a Internet fijo por tecnologia y localidad:
Es el df2

Este era importante ya que contenia informacion sobre las Capitales y el tipo de Servicio
-Todas las capitales tienen tipos de servicios que son diferentes entre si
-El motivo de ver cual es el mayor tipo de servicio por capital  es el que puede ser un punto de partida para luego agregar a las localidades que se encuentren proximas.
Por ejemplo si elijo Formosa el mayor tipo de servicio es wirelles el cual podriamos usar tambien para localidades cercanas por lo que es mucho mas facil empezar con instalaciones o recursos que ya esten e ir expandiendo que empezar o crear todo de cero.

Acceso a Internet Fijo Por velocidad de Bajada y Localidad
Es df3

Este dataset tenia muchisima informacion, en el EDA solo se toma las velocidades mas bajas y se analizo como un caso de ejemplo a la Provincia de Formosa
-Analizamos por ejemplo la provincia de Formosa
-El total de los Departamentos (Partidos) de la Provincia de Formosa tienen areas con mbps bajo.
-El porque se dio todos los departamentos puede deberse que pese a que hay localidades con muy buen internet no todo el departamento esta cubierto por lo cual aunque aunque halla una localidad que no cuente con internet esto nos incluira a nuestros calculos a ese departamente al que pertenece por lo que este resultado debe tomarse con precacucion.

Internet accesos por tecnologia
Es df4

-Wirelles se mantiene constante, pero ADSL tuvo una caida con los anos, otro servicio que tuvo aumentos fue Cablemodem y Fibra optica, sin embargo en el ultimo tiempo Cablemodem disminuyo.
Podriamos teorizar que posiblemente por el aumento de fibra optica pero necesitaremos pruebas estadisticas para corrobarar esta hipotesis.

Internet BAF
Se uso el como dataset el df5

-Capital y Cordoba son las que tienen menor Banda ancha fija, podemos plantear de nuevo que podria deberse a que son Provincias Grandes y muy heterogeneas en cuanto a las ciudades.

Internet Ingresos
Usamos como dataset el df6

-Desde el 2014 a 2022, los Trimestres con mas ingresos son: Abr-Jun y Jul-Sept, por lo deberiamos prestar atencion a este dato.

Internet Penetracion
Usamos df7

- Capital Federal es el distrito con mayor numero, esto es de esperarse ya que es la capital de la Argentina en la cual hay muchas empresas y tecnologias asentadas alli
- Santiago del Estero es la Provincia con menor Acceso por cada 100 hogares, en principio habria que hacer un analisis particular del porque de esto. Algunas hipotesis: Muchos hogares sin necesidades sastifechas? Politicas centralizadas hacia la capital? Pueblos chicos y dispersos?

- Localidades con Conectividad
Este data es complementario al df1, ya que ahora contamos con la informacion de 4G, 3G, Telefonia fija y Satelital, por eso es que fue seleccionado.

Se uso como dataset el df8

-Hay una gran diferencia entre las Provincia de Buenos Aires con respecto a las demas, las que siguen son Cordoba y Santa Fe esto podemos explicar ya que estas 3 Provincias son los centros mas grandes de Argentina en cuanto a poblacion y economia.

Velocidad media de bajada de Internet fijo por provincias
Usamos el df9

El Mayor valor de mbps es Capital Federal, seguido por Provincia de Buenos Aires por un lado y por otro al final del grafico tenemos que las menores son las 3 Provincias correspondientes a la Region de la Patagonia, esto podemos tratar de inferir que podria haber un componente geografico y de superficie que hace que a pesar de tener internet en los grandes centros muchos pueblos todavia estan aislados.
Para dar mas peso a esto es conveniente analizar en conjunto con el df3 ya que tiene datos de mbps y Localidad.

Denuncias y Reclamos
Se usaron el df10 y el d11

- Telecom y Telefonica son los operadores con mayores reclamos y entre tipo de reclamos los Problemas Tecnicos son los mas elevados.
- Esto es importante a tenerlo en cuenta ya que no nos sirve brindar servicios que no sean de buena calidad
- 2 empresas concentran la mayor parte de Reclamos y Denuncia. Lo mas interesante es aqui aparece de nuevo Telefonica, la cual en el grafico anterior era una de las que mayores problemas tecnicos presentaba.

# Dataset usados en el Dashboard
-A la izquierda hay un panel de visualizaciones para interactuar

->Visualizacion1: Acceso a Internet fijo por tecnología y provincia.

->Visualizacion2: Internet_Accesos-por-tecnologia.

->Visualizacion3: Internet_Accesos-por-tecnologia.

->Visualizacion4: Velocidad media de bajada de Internet fijo por provincia.

->Visualizacion5: Denuncias_y_reclamos_202306-1.

# Resumen

En resumen, se encontraron diferencias en la distribución de tecnologías de internet entre provincias y regiones de Argentina. La fibra óptica fue el servicio que más creció trimestre a trimestre, especialmente en las provincias de la región de la Patagonia. También se observó que las provincias pertenecientes a una misma región tenían tipos de servicio heterogéneos.

En cuanto a los accesos a internet fijo por tecnología y localidad, cada capital tiene tipos de servicios diferentes, lo cual podría ser útil para expandir servicios a localidades cercanas. Además, se identificaron áreas con velocidades de bajada bajas en todos los departamentos de la provincia de Formosa.

En términos de tipos de tecnología de acceso a internet, el servicio inalámbrico se mantuvo constante, mientras que el ADSL disminuyó y la fibra óptica y el cablemódem experimentaron aumentos, aunque recientemente el cablemódem ha disminuido. Se plantea la hipótesis de que esto podría estar relacionado con el aumento de la fibra óptica.

En conclusión, se observaron diferencias significativas en la distribución de tecnologías de internet en Argentina. Las provincias de la región de la Patagonia destacaron por tener altos valores de fibra óptica, mientras que las provincias más grandes y heterogéneas, como Buenos Aires y Córdoba, presentaron menor acceso a banda ancha fija. Es importante considerar estas disparidades para mejorar la calidad y el alcance de los servicios de internet en todo el país. Además, se destaca la necesidad de abordar los problemas técnicos y las quejas de los usuarios para garantizar una mejor experiencia en el acceso a internet.

# Contacto o sugerencias

mail: rodribogado50@gmail.com
