Algoritmo Ejerciciocuatro
	//realizar un pseudocodigo que permita mostrar 20 productos con su numero
	// de serie stock y precio
	productos = ""
	para i<-1 hasta 20
		Escribir "Ingrese nombre producto"
		leer nproducto
		Escribir  "Ingrese numero de serie"
		leer nserieproducto
		Escribir "Ingrese stock del producto"
		leer nstockproducto
		Escribir "Ingrese precio del producto"
		leer precio
		//productos="Nombre "+nproducto+" Numero serie "+nserieproducto+" Numero de stock "+nstockproducto+" precio "+precio
		productos=productos+" Nombre "+nproducto+" Numero serie "+nserieproducto+" Numero de stock "+nstockproducto+" Precio "+precio
	FinPara
	Mostrar productos
FinAlgoritmo
