/*  

condicionales anidados/compuestos, ternarios y ciclos?

*/

/*
x>18=nombre,dni,mail
x<18=sexo,apellido,dni
(x>18=nombre,dni,mail) U (x<18=sexo,apellido,dni)

*/

edad = prompt("Ingrese su edad");

if (edad > 18) {    //cuando se cumple edad>18
    nombre = prompt("Ingrese su nombre");
    dni = prompt("Ingrese su dni");
    mail = prompt("Ingrese su mail");
    document.writeln("El nombre:" + nombre);
    document.writeln("El dni: " + dni);
    document.writeln("El mail: " + mail);
}
if (edad < 18) {
    sexo = prompt("Ingrese su sexo");
    apellido = prompt("Ingrese su apellido");
    dni = prompt("Ingrese su dni");
    document.writeln("El sexo:" + sexo);
    document.writeln("El apellido: " + apellido);
    document.writeln("El dni: " + dni);
}
/*
Prevencion de errores
*/
if (edad == 18) {
    alert("Edad ingresada no valida");
}

// al no ingresar nada sale un alerta
if (edad == null) {
    alert("No ha ingresado ningun valor");
}