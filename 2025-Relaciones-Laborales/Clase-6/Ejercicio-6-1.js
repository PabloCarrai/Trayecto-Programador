/*
Codificar un programa  en javascript que permita almacenar 
en un vector 10 edades. Mostrar por html las 10 edades.  
En otro vector almacenar 10 nombres y mostrarlos por consola. 
Por ultimo se pide un vector que ingrese distintos grupos musicales 
y luego mostrarlo por consola con alerta
*/

//1 Parte
diezEdades = []
for (let x = 0; x < 3; x++) {
    diezEdades[x] = prompt("Edad?   ")
}
for (let x of diezEdades) {
    document.writeln(`<li>Edades: ${x} </li>`)
}

//2 Parte
diezNombres = []
for (let x = 0; x < 3; x++) {
    diezNombres[x] = prompt("Nombre?   ")
}
for (let x of diezNombres) {
    console.log(`Nombre: ${x} `)
}

//3 Parte
diezNombresBandas = []
for (let x = 0; x < 3; x++) {
    diezNombresBandas[x] = prompt("Banda?   ")
}
for (let x of diezNombresBandas) {
    console.warn(`Banda: ${x} `)
}
