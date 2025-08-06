/* 
Vectores/arrays
*/

//array de 4 elementos
let verduras = ["Tomate", "Lechuga", "Cebolla", "Papas"]
// los elementos tienen indices
//                  0       1           2        3
console.log(verduras[2])
console.log(verduras[3])
console.log(verduras[9]) //undefined 
console.log(verduras[0])
verduras[21] = "frutilla" //podemos definir valores en cualquier indice
console.log(verduras[21]) // esto cambio la cantidad de elementos del array
console.log(verduras.length)
for (let x = 0; x < 21; x++) {
    verduras[x] = prompt("Ingrese verduras")
}
console.log(verduras)