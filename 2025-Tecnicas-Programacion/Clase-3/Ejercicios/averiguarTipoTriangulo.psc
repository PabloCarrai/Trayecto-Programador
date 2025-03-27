Algoritmo averiguarTipoTriangulo
	Escribir 'vamos a analizar un triangulo y dado sus lados sabremos su tipo, es decir, si es escaleno, equilatero e isosceles'
	Escribir 'Ingrese un lado del triangulo'
	Leer lado1
	Escribir 'Ingrese otro lado del triangulo'
	Leer lado2
	Escribir 'Ingrese el ultimo lado del triangulo'
	Leer lado3
	Si lado1==lado2 Y lado2==lado3 Entonces
		Escribir 'Es un triangulo equilatero'
	SiNo
		Escribir 'No es un triangulo equilatero'
	FinSi
	Si lado1<>lado2 Y lado2<>lado3 Entonces
		Escribir 'Es Triangulo Escaleno'
	SiNo
		Escribir 'No es triangulo Escaleno'
	FinSi
	Si (lado1==lado2 Y lado1<>lado3) O (lado1==lado3 Y lado1<>lado2) O (lado2==lado3 Y lado2<>lado1) Entonces
		Escribir 'Es triangulo Isosceles'
	SiNo
		Escribir 'No es triangulo isosceles'
	FinSi
FinAlgoritmo
