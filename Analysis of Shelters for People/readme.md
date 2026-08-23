# Análisis de Datos para la Gestión de un Refugio de Personas

## Descripción General del Proyecto

En este proyecto, abordé un análisis de datos enfocado en la gestión y las dinámicas operativas de un refugio de personas. Mi objetivo principal fue utilizar el análisis de datos para comprender mejor las características demográficas de los ocupantes, identificar patrones en sus necesidades de servicio y evaluar la asignación de recursos. Este trabajo me permitió aplicar mis habilidades analíticas en un contexto de impacto social, extrayendo información crucial para la optimización de la ayuda humanitaria.

## Dataset

Para este análisis, generé un dataset de ejemplo directamente en Python, simulando datos de ocupantes y servicios de un refugio. El dataset incluyó variables como la edad, el género, la nacionalidad, la fecha de llegada, el servicio principal requerido, la duración de la estancia, condiciones especiales y el número de familiares alojados.

## Herramientas y Librerías Empleadas

Utilicé Python como mi principal herramienta de programación. Mis librerías fundamentales para este proyecto fueron Pandas, para la manipulación y el análisis de datos, y Matplotlib junto con Seaborn para la creación de visualizaciones claras y perspicaces. Todo el trabajo fue realizado en Google Colab, proporcionando un entorno de desarrollo interactivo y accesible.

## Análisis

Mi proceso comenzó con la exploración inicial de datos, utilizando funciones como `info()` y `describe()` para entender la estructura, los tipos de datos y las estadísticas básicas de las variables. Esto confirmó la limpieza y preparación del dataset para el análisis.

Posteriormente, me enfoqué en el análisis de las características de los ocupantes. Examiné la distribución por género y nacionalidad, encontrando una composición diversa con necesidades potencialmente diferentes entre poblaciones locales y migrantes. Realicé un análisis detallado de los servicios principales requeridos, identificando cuáles eran los más demandados y visualizando estas prioridades en gráficos de barras.

Un paso crucial fue el análisis cruzado de los servicios requeridos por nacionalidad. Este reveló que las necesidades de alojamiento son particularmente pronunciadas entre la población migrante, mientras que la población local presenta una demanda más distribuida incluyendo comida y asesoría legal. También exploré la distribución de edades a través de un histograma, lo que me permitió identificar grupos etarios específicos con posibles necesidades particulares. Finalmente, analicé las 'Condiciones Especiales' de los ocupantes, reconociendo la presencia de menores, personas con enfermedades crónicas y discapacidad, lo cual es vital para la planificación de atención especializada. La duración de la estancia también fue analizada, proporcionando *insights* sobre la rotación de ocupantes.

![img1](servi_reque.png)

![img1](servi_reque_pornacio.png)

![img1](distriedas.png)

![img1](distriestan.png)

## Conclusiones

Los hallazgos sobre la composición de la población, las necesidades de servicio diferenciadas por nacionalidad y la identificación de condiciones especiales son fundamentales para la gestión eficaz de un refugio. Comprender estas dinámicas es esencial para optimizar la asignación de recursos y mejorar la calidad de la atención proporcionada a las personas en situación de vulnerabilidad.

---

[Enlace a mi Cuaderno de Colab en GitHub](https://colab.research.google.com/drive/10VLiVqh2TDQ5sB2Vnnk0pt2OsdtXd8zv?usp=sharing)
