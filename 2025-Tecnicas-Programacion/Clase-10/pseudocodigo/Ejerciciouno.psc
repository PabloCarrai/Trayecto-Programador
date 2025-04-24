Algoritmo Ejerciciouno
	cmf<-0
	Escribir "Vamos a probar su conocimiento sobre marcas de auto"
	Escribir "Ingrese marcas de autos de Ferrari que conosca"
	Escribir "Quiere participar?"
	leer respuesta
	Mientras respuesta="si" O respuesta="Si" Hacer
		Escribir "Ingrese marcas de autos de Ferrari que conosca"
		leer marca
		Si marca="ferrari" O marca="Ferrari" Entonces
			Escribir "Esa si es marca Ferrari ",marca
			cmf<-cmf+1
		SiNo
			respuesta="no"
		FinSi
	Fin Mientras
	Escribir "Cantidad de ferraris ", cmf
FinAlgoritmo
