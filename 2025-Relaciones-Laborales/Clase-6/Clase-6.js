//Vector en Js
let tecnologia = ["Mouse", 1500, 1, 0, 1010]
//permite guardar una lista de elementos de diferentes tipos
console.log(tecnologia[0])
tecnologia[90] = "Valeria"
//Ingresar datos al vector
for (let x = 5; x <= 10; x++) {
    tecnologia[x] = prompt("Ingrese un dato")
}
for (let u = 0; u <= tecnologia.length; u++) {
    console.log(tecnologia[u])
}
for (let j of tecnologia) {
    console.log(j)
}