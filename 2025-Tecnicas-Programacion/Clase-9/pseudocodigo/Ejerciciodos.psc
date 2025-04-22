Algoritmo Ejerciciodos
	// necesito procesar el total de la compra de 50 productos
	acumulador<-0 // <- == a =
	Para x<-1 Hasta 50 con paso 1 Hacer
		Escribir "Sr operador ingrese el precio del producto"
		leer precio
		acumulador <- acumulador+precio
		// acumulador = acumulador+otra_variable
	FinPara
	// muestro el total fuera del ciclo
	Escribir "El total es ",acumulador
FinAlgoritmo
