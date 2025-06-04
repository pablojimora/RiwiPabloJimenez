cantidad_de_coordenadas:int=int(input("Ingrese la cantidad de coordenadas que se va a ingresar"))
coordenadas_cuadrante_1=[]
coordenadas_cuadrante_2=[]
coordenadas_cuadrante_3=[]
coordenadas_cuadrante_4=[]

for i in range(cantidad_de_coordenadas):
    x:float=float(input(f"Ingrese la coordenada x {i+1}"))
    y:float=float(input(f"Ingrese la coordenada y {i+1}"))

    if x>0 and y>0:
        coordenadas_cuadrante_1.append(x)
        coordenadas_cuadrante_1.append(y)

    elif x<0 and y>0:
        coordenadas_cuadrante_2.append(x)
        coordenadas_cuadrante_2.append(y)

    elif x<0 and y<0:
        coordenadas_cuadrante_3.append(x)
        coordenadas_cuadrante_3.append(y)

    elif x>0 and y<0:
        coordenadas_cuadrante_4.append(x)
        coordenadas_cuadrante_4.append(y)

    else:
        print("Su coordenada es 0,0 esta en la mitad del plano cartesiano")

print(f"Las coordenadas del cuadrante 1 son: {coordenadas_cuadrante_1}")
print(f"Las coordenadas del cuadrante 2 son: {coordenadas_cuadrante_2}")
print(f"Las coordenadas del cuadrante 3 son: {coordenadas_cuadrante_3}")
print(f"Las coordenadas del cuadrante 4 son: {coordenadas_cuadrante_4}")
