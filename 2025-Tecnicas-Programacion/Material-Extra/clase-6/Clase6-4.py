def Suma(a,b):
    return a+b
def Resta(a,b):
    return a-b

print(Suma(2,1))
print(Resta(3,2))
print(Suma(4,3))
print(Resta(9,15))

ResultadoResta=Resta(4,5)
#Opcion 1
print(Suma(ResultadoResta,9))

#Opcion 2
print(Resta(Suma(5,4),5))


#Opcion 3
ResultadoResta=Resta(6,9)
ResultadoSuma=Suma(4,4)
print(Suma(ResultadoResta,ResultadoSuma))