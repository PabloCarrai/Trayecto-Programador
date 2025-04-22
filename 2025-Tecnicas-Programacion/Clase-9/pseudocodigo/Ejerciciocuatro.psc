Algoritmo Ejerciciocuatro
	//Realizar pseudocodigo que permita mostrar el total de personas
	//mayores a 18 y la cantidad de personas sexo femeninos en 12 personas. 
	sfemenino<-0
	medad<-0
	Para i<-1 Hasta 12 Con Paso 1 Hacer
		Escribir "Ingrese su sexo"
		leer sexo
		Escribir "Ingrese su edad"
		leer edad
		Si edad>17 Entonces
			medad<-medad+1		
		FinSi
		Si sexo="femenino" Entonces
			sfemenino<-sfemenino+1
		FinSi		
	Fin Para
	Escribir "Cantidad de mayores a 18 años"
	Escribir medad
	Escribir "Cantidad de persona sexo femenino"
	Escribir sfemenino
	
FinAlgoritmo
