/*

Codificar en javascript un programa que muestre
 la personas que tienen 33 años. 
 Si tiene 33 años mostrar el nombre, dni y mail. 
 Si no tiene 33 años mostrar el apellido, dirección 
 y codigo postal.

 */
edad = parseInt(prompt("Ingrese su edad "));
if (edad == 33) {
    nombre = prompt("Ingrese su nombre");
    dni = prompt("Ingrese su dni");
    mail = prompt("Ingrese su mail");
    document.writeln("Nombre: " + nombre);
    document.writeln("DNI: " + dni);
    document.writeln("Mail: " + mail);
}
if (edad != 33) {
    apellido = prompt("Ingrese su apellido ");
    direccion = prompt("Ingrese su direccion");
    cpostal = prompt("Ingrese su codigo postal");
    document.writeln("Apellido: " + apellido);
    document.writeln("Direccion: " + direccion);
    document.writeln("Codigo postal: " + cpostal);
}

