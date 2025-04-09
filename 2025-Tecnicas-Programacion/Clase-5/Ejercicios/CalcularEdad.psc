Algoritmo CalcularEdad
	Escribir "Ingrese su nombre"
	Leer Nombre
	Escribir "Ingrese su DNI"
	Leer DNI
	Escribir "Ingrese su año de nacimiento"
	Leer añoNacimiento
	Escribir "Ingrese el año actual"
	leer añoActual
	Escribir "Su Nombre es",Nombre
	Escribir "Su DNI es ",DNI
	Escribir "Su edad es ",añoActual-añoNacimiento
	Si ((añoActual-añoNacimiento)<18) Entonces
		Escribir "Usted es Menor de edad"
	SiNo
		Escribir "Usted es mayor de edad"
	FinSi
	
FinAlgoritmo
