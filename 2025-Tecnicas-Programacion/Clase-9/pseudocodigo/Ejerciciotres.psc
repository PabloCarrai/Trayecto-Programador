Algoritmo Ejerciciotres
	//contar los mayores a 18 en un registro de 10 personas
	Cmayor<-0
	Para i<-1 hasta 10 Hacer
		Escribir "Ingrese la edad"
		leer edad
		Si edad>=18 Entonces
			// Contador
			Cmayor<-Cmayor+1
		FinSi
	FinPara
	Escribir "Cantidad de mayores a 18 "
	Escribir Cmayor	
FinAlgoritmo
