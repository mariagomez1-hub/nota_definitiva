# nota_definitiva
Programa en Python paracalcular la nota definitiva de una asignatura en el Colegio Guanentá.

## Análisis

### Variables de entrada
- nc: Nota cognitiva
- np: Nota procedimental
- na: Nota actitudinal
- au: Autoevaluacion
- bi: Bimestral 

### Procesamiento
- nd: Nota definitiva

$nd = 0.3*nc+0.3*np+0.1*na+0.1*au+0.2*bi$

## Diseño

![Diagrama de flujo](diagrama.png)

## Construcción
- codigo implemento en el archivo nota_definitiva.py