# Aura Jalisco 

## Resumen

Desarrollar un sistema de gestión energética inteligente basado en algoritmos de
Inteligencia Artificial para la regulación dinámica de la generación distribuida solar
en el estado de Jalisco, con el fin de mitigar la saturación térmica de los
transformadores de red, garantizar la estabilidad del voltaje y promover la
soberanía energética bajo un enfoque de justicia ambiental y eficiencia operativa.

## Planteamiento del problema

El proyecto surge de la necesidad de Jalisco de contar con alternativas para producir y aprovechar energía más limpia, sin depender tanto de fuentes externas de energía.
Además, el crecimiento de las actividades agrícolas y el uso de los recursos naturales han generado una mayor presión sobre los ecosistemas, contribuyendo a los problemas de contaminación ambiental que enfrenta el estado.
Ante esta situación, Aura Jalisco busca analizar y proponer alternativas que ayuden a reducir la huella de carbono, aprovechar mejor los recursos naturales e impulsar el uso de energías renovables.
Una de las principales propuestas es utilizar Inteligencia Artificial para mejorar la gestión de la energía solar y ayudar a prevenir problemas en la infraestructura eléctrica.

## ¿Cómo funciona la aplicación?

Actualmente, Aura Jalisco cuenta con una API desarrollada con FastAPI, que permite cargar y analizar datos históricos de irradiación solar, entrenar un modelo de Machine Learning y realizar predicciones.
La aplicación utiliza información de radiación solar obtenida de NASA POWER y un modelo de árbol de decisión para estimar la irradiación solar de una fecha determinada.

### Funciones principales

- **Subir archivos CSV:** permite cargar los datos históricos de irradiación solar.
- **Consultar datasets:** muestra los archivos que se han registrado.
- **Consultar estadísticas:** permite revisar información estadística de los datos.
- **Revisar valores faltantes:** muestra si existen datos vacíos.
- **Consultar información:** permite conocer las columnas y los tipos de datos del archivo.
- **Analizar datos:** muestra un resumen de las columnas numéricas y sus correlaciones.
- **Entrenar el modelo:** procesa los datos y entrena el algoritmo de Machine Learning.
- **Realizar predicciones:** permite indicar una fecha para obtener una estimación de irradiación solar.

## ¿Cómo ejecutar la aplicación?

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/EnriqueGR123/Aura-Jalisco.git
   ```

2. Entrar a la carpeta del proyecto:

   ```bash
   cd aura-jalisco
   cd backend
   ```

3. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

4. Activar el entorno virtual:

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Mac / Linux:**
   ```bash
   source venv/bin/activate
   ```

5. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Configurar la conexión a PostgreSQL en el archivo `.env` y asegurarse de que la base de datos esté disponible.

7. Ejecutar la aplicación:

   ```bash
   uvicorn app.main:app --reload
   ```

## ¿Cómo utilizar la aplicación?

Una vez iniciada la API, abrir la siguiente dirección en el navegador:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Desde ahí se pueden utilizar las rutas de la aplicación:

1. **Subir el CSV:** utilizar `POST /datasets/` y seleccionar el archivo de irradiación solar.
2. **Consultar los datos:** utilizar las rutas de consulta para revisar la información del archivo.
3. **Entrenar el modelo:** utilizar `POST /datasets/{id}/train`, colocando el ID del dataset que se desea entrenar.
4. **Realizar una predicción:** utilizar `POST /datasets/{id}/predict` e indicar la fecha deseada.

Ejemplo de los datos que se deben enviar para una predicción:

```json
{
  "fecha": "2027-06-15"
}
```

La aplicación devuelve una estimación de irradiación solar expresada en `kWh/m2/dia`.

## Documento completo del proyecto

Para conocer más sobre Aura Jalisco, sus objetivos, marco teórico, impacto social y propuesta de solución, puedes consultar el siguiente documento:

[📄 Ver documento completo de Aura Jalisco](docs/aura_jalisco.pdf)

## Objetivo a futuro

Se busca que Aura Jalisco siga creciendo y pueda integrar más información, como datos del clima, consumo eléctrico y mediciones de sensores. Esto permitiría desarrollar herramientas más completas para apoyar la gestión energética y el aprovechamiento de las energías renovables en Jalisco.