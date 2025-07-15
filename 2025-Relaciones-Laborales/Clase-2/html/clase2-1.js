numero1=prompt("Ingrese un valor");
numero2=prompt("Ingrese otro numero");
// lo paso a entero
numero1=parseInt(numero1)
numero2=parseInt(numero2)
suma=numero1+numero2;
resta=numero1-numero2;
multiplicacion=numero1*numero2;
division=numero1/numero2;
potencia1=numero1**2;
potencia2=numero2**2;
console.warn("La suma es "+suma);
console.warn("La resta es "+resta);
console.info("La multiplicacion es "+multiplicacion);
console.info("La division es "+division);
console.info("La potencia del primer numero "+potencia1);
console.info("La potencia del segundo numero "+potencia2);