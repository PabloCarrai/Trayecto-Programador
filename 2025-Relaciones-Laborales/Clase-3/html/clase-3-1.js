/*
Operador ternario
*/

/*

if(n1>18){
    //verdad
    console.warn("Esto pasa por verdad")
}else{
    console.error("No se cumple la condicion")
}

*/

/*

(n1>18)
"Esto pasa por verdad"
"No se cumple la condicion"

//lo unimos

(n1>18) ? "Esto pasa por verdad" : "No se cumple la condicion"

*/

// Lo mostramos 
n1 = 1;
console.info((n1 > 18) ? "Esto pasa por verdad" : "No se cumple la condicion")

/*

n1=3;
n2=2;
n3=1;

if(n1>n2 && n1==n3){
    alert("El mayor es: "+n1)
}else{
    if(!(n2<n3&&n2<n1)){ //niego con !
    alert("El mayor es: "+n2)
    }else{
        if(n3>=n2 ||n3>=n1){
        alert("El mayor "+n3)
    }}
}

&&  y
||  o
!   negacion

*/