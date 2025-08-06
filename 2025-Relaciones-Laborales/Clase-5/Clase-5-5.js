/*
let frutas = []
for (let x = 0; x < 10; x++) {
    frutas[x] = prompt("Ingrese una fruta")
}
for (let x = 0; x < 10; x++) {
    document.writeln(`<p>${frutas[x]}</p>`)
}

let frutas = []
for (let x = 0; x < 3; x++) {
    frutas[x] = prompt("Ingrese una fruta")
}
for (let i in frutas) {
    document.writeln(`<p>${frutas[i]}</p>`)
}
*/
let frutas = []
for (let x = 0; x < 3; x++) {
    frutas[x] = prompt("Ingrese una fruta")
}

for (let i of frutas) {
    document.writeln(`<p>${i}</p>`)
}