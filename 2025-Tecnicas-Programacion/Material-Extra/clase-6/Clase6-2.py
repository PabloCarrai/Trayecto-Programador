def Resta():
    a=1#Valor local
    b=2#Valor local
    resta = a-b
    return resta

a=99#Valor Global
b=55#Valor Global
print(Resta())
print(a)
print(b)
#Valor Global, quiere decir, que si yo le doy un valor por afuera de un bloque de código o de una función. El valor de la variable, no va a cambiar, a no ser que se modifique internate, es decir, que se le asigne otro valor. Si no, va a seguir valiendo lo mismo.

#Valor Local, quiere decir, que dentro de ese bloque de código o de una función, el valor, va a ser el que se le asigne de manera interna, es decir, en ese bloque de código.