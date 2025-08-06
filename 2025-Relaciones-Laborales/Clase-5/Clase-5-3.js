// Guardando en una variable el texto almacenado
let ingreso = document.getElementById("pass")
let boton = document.getElementById("btnpass")
boton.addEventListener("click", function () {
    if (ingreso.type == "text") {
        ingreso.type = "password"
        boton.textContent = "Mostrar Contraseña"
    } else {
        ingreso.type = "text"
        boton.textContent = "Ocultar Contraseña"
    }
})