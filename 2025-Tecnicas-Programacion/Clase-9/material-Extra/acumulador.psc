Algoritmo sin_titulo
	//Necesito un programa que procese el 
	//total de una compra de 50 productos y vaya mostrando el total acumulado
	Total<-0
	Para X<-1 Hasta 5 Hacer
		Escribir "Sr. Op. Ingrese el precio de producto"
		Leer Precio
		//Acumulador
		Total<-Total + Precio
		Escribir "Sr Op. Ingrese el descuento"
		Leer Descuento
		//Acumulador negativo
		Total<-Total - Descuento
		//Variable=Variable+OtraVariable
		//Mostrar Dentro del ciclo en este caso estaria mal
		//Muestro el total acumulado por cada precio ingresado
		Escribir "De momento el total es:"
		Escribir Total
	FinPara
	//Mostrar total final -> Fuera del ciclo
	Escribir "El total de la compra es:"
	Escribir Total
FinAlgoritmo
