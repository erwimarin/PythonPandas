# PythonPandas

Introdución:

Se recuperan de la siguiente página los datos de la Organización territorial de Chile y se da un resultado en csv.
https://es.wikipedia.org/wiki/Chile

Indicaciones de la operación:

* Se requiere limpiar los datos eliminando la columna "Mapa administrativo" y "Organización territorial de Chile".
* Renombrar las columnas a 'Región', 'Población', 'Superficie', 'Densidad', 'Capital'.
* Eliminar último registro que contiene el total  de las columnas.
* Crear función que obtenga el % de la Población.
* Agregar nueva columna con los porcentajes del punto anterior.
* Exportar la información en archivo CSV.

Se requiere instalar las libreria indicadas en el archivo requirements.txt.

beautifulsoup4 == 4.8.1 
html5lib == 1.0.1 
lxml == 4.4.1
numpy == 1.17.3 
pandas == 0.25.2
