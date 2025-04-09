Algoritmo BronceH
	acumulador=0
	clientes = 5
	Mientras 0 < clientes Hacer
		Escribir "Ingrese el gasto del cliente"
		leer gasto
		acumulador = acumulador + gasto
		clientes = clientes -1
	Fin Mientras
	Escribir "El gasto total es ",acumulador
	
FinAlgoritmo
