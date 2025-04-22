Algoritmo sin_titulo
	//Mostrar el total de personas con 18 años en un registro de 10 personas
	Cmayor<-0
	Para P<-1 Hasta 10 Hacer
		Escribir "Sr. Op. Ingrese su edad:"
		Leer Edad
		Si Edad>=18 Entonces
			Cmayor<-Cmayor+1
		SiNo
			Cmayor<-Cmayor-1
		FinSi
	FinPara
	Escribir "La cantidad de personas mayores es: ",Cmayor
FinAlgoritmo
