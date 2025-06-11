Edades=[21,2,3,4,15,33]
i=0
for x in Edades:
    print(x)
while(len(Edades)>0):
    Edades.remove(Edades[i])
    
for x in range(5):
    valor=int(input("Ingrese una edad: "))
    Edades.insert(0,valor)

for x in Edades:
    print(x)