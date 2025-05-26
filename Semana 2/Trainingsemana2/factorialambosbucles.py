#con for
numero:int=(int(input("Ingrese el numero de factorial que quiera")))
resultado=1
for i in range(numero,0,-1):
    resultado = resultado * i
print(resultado)
