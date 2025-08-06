/*
do while 
*/

/*
do {
    console.log("Marina Cuenca")
}
while (confirm("Desea continuar"))

do{
    var edad=parseInt(prompt("Ingrese edad"))
}while(edad!=0)

*/

/* 
while si o si hay que cumplir la condicion antes de entrar 
*/
/*
edad = 18
while (edad == 18) {
    console.log("mauro")
    edad = parseInt(prompt("Ingrese edad"))
}
*/

/*
Realizar un programa en javascript que ingrese distintos 
nombres de paises, cuando ingrese argentina 
debe imprimir todos los paises ingresados 
con color de fondo celeste y color de letra blanco por html
*/

var contador = 0
do {
    contador = contador + 1
    pais = prompt("Ingrese nombre del pais ")
    document.writeln(`<p><spam style="background-color:skyblue;color:white;">${pais}</spam></p>`)

}
while (pais != "argentina")
document.writeln(contador)