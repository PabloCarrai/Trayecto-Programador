/*
 
  Codificar un programa en javascript que permita el ingreso de 
  distintos ramales de una terminal de trenes. 
  Mostrar por html (document.writeln) la cantidad de trenes 
  que hay disponibles para el ramal suarez. 
  Mostrar por aleta la cantidad de trenes que hay disponibles 
  para el ramal mitre. y mostrar por consola la cantidad de trenes 
  que hay disponibles para el ramal tigre

  */
// cantidad de tremes ramal suarez
suarez = parseInt(prompt("Cuantos trenes dispone el ramal Suarez? "));
mitre = parseInt(prompt("Cuantos trenes dispone el ramal Mitre? "));
tigre = parseInt(prompt("Cuantos trenes dispone el ramal Tigre? "))
document.writeln("El ramal suarez dispone de " + suarez);
alert("Cantidad de trenes del ramal Mitre " + mitre);
alert("Cantidad de trenes del ramal Tigre " + tigre);