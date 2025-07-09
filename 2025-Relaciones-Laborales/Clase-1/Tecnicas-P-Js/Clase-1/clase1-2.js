// salidas por html como tal, algo visual
document.write("Esto es una Salida que se visualizara como contenido del sitio");
// equivalente al document.write, agrega el texto en una nueva linea
document.writeln("Otro texto");
// variables
auto = 21;    //definimos y le damos el valor a la variable
alert(auto);
alert(auto + "21");
alert(auto + 1);
alert(auto / 2);
alert(auto * 3.14);
// no somos esclavos por determinar el tipo de datos
/* 
sin importar el tipo de datos del valor de la variable
las operaciones que se realizan van a depender del tipo de datos
*/

color = "Rojo";
alert(color * 3.14);  // devuelve un NaN no es una operacion el valor no es un numero
alert(color + 1);
alert(color / 2);
alert(color * 3.14);