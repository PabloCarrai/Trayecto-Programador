//  matrices de 2 dimensiones y multidimensionales
//  Una tabla por ejemplo filas y columnas
//  columna, nombre, edad, dni
//  filas datos ingresados en columnas

//  columna
datos = ["nombre", "edad", "dni", "fecha"]
//  fila
c1 = ["Maria", 22, 233234, 30211233]
c2 = ["Mario", 12, 454334, 30211213]

console.log(datos)
console.log(c1)
console.log(c2)

console.log(datos[0], c1[0], c2[0])
console.log(datos[1], c1[1], c2[1])

//convertimos a matriz
Persona = [
    ["Nombre", "Edad", "DNI", "Fecha"],
    ["Jimena", 15, 34432234, 23334443],
    ["Marcos", 45, 3443114, 23334748],
    ["Ricardo", 25, 34433234, 23536443]
]
console.log(Persona)
console.log(Persona[0][0])
console.log(Persona[2][2])
console.log(Persona[3][3])

//visualizar todo
for (let i in Persona) {
    document.writeln("<br>" + [i])
    for (let j in Persona[i]) {
        document.writeln(Persona[i][j])
    }
}

//Otra forma
for (let fila = 0; fila < 4; fila++) {
    document.writeln("<br>" + Persona[fila])
}