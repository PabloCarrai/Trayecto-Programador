/*
Realizar en javascript 2 funciones, 
una sin parametros y otra con parametros. 
La función sin parametro debe calcular 
el perímetro y área de un cuadrado. 
La función con parametro debe calcular 
y verificar si un número ingresado 
por el usuario es par. Si es par mostrar 
un texto de color verde por html diciendo 
"Es par", si no es par debe mostrar un texto
 de color rojo por html diciendo "No es par :("
*/

function esPar(numero) {
    if (numero % 2 == 0) {
        document.writeln(`<p style="color:green">Es Par</p>`)
    } else {
        document.writeln(`<p style="color:red">No Es Par</p>`)
    }
}
let numero = parseInt(prompt("Ingrese un numero "))
esPar(numero)

function calculoPCuadrado() {
    let lado = parseInt(prompt("Ingrese lado del cuadrado"))
    document.writeln(`El perimetro de lado ${lado} es ${lado * 4}`)
    document.writeln(`<br>El area de lado ${lado} es ${lado * lado}`)
}
calculoPCuadrado()