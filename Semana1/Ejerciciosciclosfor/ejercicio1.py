cantidad_numeros:int=int(input("Cuantos numeros vas a validar"))
validacion=[]
numeros_seleccionados=[]
for i in range(cantidad_numeros):
    numeros=float(input("Ingrese el numero a validar"))
    if numeros >=1000:
     validacion.append(numeros)

print(validacion)