/*
Codificar un script que acepte 2 numeros ingresados por el usuario 
y que permita mostrar la suma entre esos dos numeros, la resta, 
la multiplicación, la división y la potencia  al cuadrado de cada uno. 
Se deben mostrar todos los resultados por consola, 
y al menos 2 por error
*/

numero1 = prompt("Ingrese un numero");
numero2 = prompt("Ingrese otro numero");
console.error("La suma es igual a ", numero1 + numero2);
console.log("La resta es igual a ", numero1 - numero2);
console.log("La division es igual a ", numero1 / numero2);
console.log("La multiplicacion es igual a ", numero1 * numero2);
console.log("La potencia de 2 del primer numero es igual a ", numero1 ** 2);
console.error("La potencia de 2 del segundo numero es igual a ", numero2 ** 2);