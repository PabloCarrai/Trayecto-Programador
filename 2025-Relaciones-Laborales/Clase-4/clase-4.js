/* 
Bucles y/o Ciclos
*/

//for (ciclo exacto)

/*
for (let x = 0; x < 50; x++) {
    console.log(x)
}
*/
/*
Programar en javascript el ingreso de 10 colores. 
Mostrar por html los distintos colores ingresados 
y mostrar por consola las vueltas que va realizando el ciclo
*/

for (let i = 1; i <= 2; i++) {
    colores = prompt("Ingrese un color ")
    document.writeln(`<p style="background-color:${colores};">${colores}</p>`)
    console.log(`${colores}`)
    console.log(`Cantidad de vueltas ${i}`)
}