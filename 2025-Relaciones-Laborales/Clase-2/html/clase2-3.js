//  condicionales
numero1 = parseInt(prompt("Ingrese un numero"));
numero2 = parseInt(prompt("Ingrese otro numero"));
//agregamos condicion divisor == 0
if (numero2 == 0) {
    console.error("No se puede dividir por 0")
} else {
    alert("La division es: " + numero1 / numero2);
}
