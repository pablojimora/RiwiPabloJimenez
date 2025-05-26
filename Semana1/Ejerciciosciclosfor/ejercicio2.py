cantidad_triangulos:int=int(input("Ingrese la cantidad de triangulos a estudiar"))
areas=[]
areas_mayores_12=[]
for i in range(cantidad_triangulos):
    base:float=float(input(f"Cual es la base del triangulo {i+1}"))
    altura:float=float(input(f"Cual es la altura del triangulo {i+1}"))
    calculo=(base*altura/2)
    areas.append(calculo)
    if calculo > 12:
        areas_mayores_12.append(calculo)

print(f"Las áreas de los triangulos son {areas}")
print(f"Las áreas mayores a 12 son: {areas_mayores_12}")

