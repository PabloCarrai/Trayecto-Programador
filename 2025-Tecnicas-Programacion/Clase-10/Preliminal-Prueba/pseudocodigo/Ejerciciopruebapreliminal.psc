Algoritmo Ejerciciopruebapreliminal
	// Realizar un pseudocodigo que permita ingresar 20 productos.
	// mostrar la cantidad de productos cuyo precio sea mayor a 1500
	cantidadP<-0
	Para i<-1 Hasta 20 Con Paso 1 Hacer
		Escribir "Ingrese nombre del producto "
		leer producto
		Escribir "Ingrese precio del mismo "
		leer precio
		Si precio>1500 Entonces
			cantidadP<-cantidadP+1
		FinSi
	Fin Para
	Mostrar "Cantidad Productos mayor a $1500: ",cantidadP
FinAlgoritmo
