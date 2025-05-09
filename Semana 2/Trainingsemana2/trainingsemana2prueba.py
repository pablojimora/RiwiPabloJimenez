cantidad_notas:int=int(input("Ingrese la cantidad de notas que se va a evaluar"))
contar_mayor:str=str(input("Desea contar calificaciones mayores a alguna calificacion?(si/no)"))
contar_especifica:str=str(input("Desea contar alguna calificacion en especifico?(si/no)"))
suma=0
contador_mayor=0
contador_especifico=0
#Listas
notas:list[float]=[]
valor_mayor_a:list[float]=[]
#Este ciclo for es el encargado de pedir la cantidad de notas que diga el usuario, validar si estan aprobadas o no, y añadirlas a la lista notas
for i in range(cantidad_notas):
    nota:float=float(input(f"Ingrese la nota numero {i+1}"))
    notas.append(nota)
    if nota >=70:
        print("Aprobado")
    else:
        print("Reprobado")
print(notas)
#Este for es el encargado de sumar las notas de la lista, para luego, fuera del for, calcular el promedio e imprimirlo

for nota in notas:
    suma = nota + suma
promedio=suma/cantidad_notas
print(f"El promedio de las notas es: {promedio}")
#En caso tal de que si quiera contar calificaciones mayores, el while funciona por medio del indice, lo que compara, es que mientras el indice sea menor
#que la cantidad de elementos que tenfa la lista notas, el ciclo sigue iterando en nota, el condicional es para que segun el indice en el que vaya
#estudie la posicion de la lista notas, ejemplo: si el indice es 1, va a leer la posicion 1, o sea el segundo valor de la lista notas, y lo va a comparar con la nota
#ingresada por el usuario, si es mayor, se agreaga a la lista de numeros mauores, y suma 1 al contador, y al indice para seguir con el siguiente elemento

if contar_mayor == "si":
    calificacionmayor:float=float(input("Ingrese la calificacion que desee comparar"))
    indice=0
    while indice < len(notas):
        if notas[indice]>calificacionmayor:
         valor_mayor_a.append(notas[indice])
         contador_mayor+=1
        indice+=1
    print(f"Hay un total de {contador_mayor} notas mayores, las cuales serian {valor_mayor_a}")
else:
    print("No se requiere comparar calificaciones")
#el ciclo for, recorre cada nota, en la lista notas, y compara con el if si nota es igual a la calificacion especifica, añade la nota a la lista de calificacion especifica
#luego suma 1 al contador e imprime cuantas notas hay
if contar_especifica == "si":
    calificacionespecifica:float=float(input("Ingrese la calificacion que desee contar"))
    for nota in notas:
        if nota == calificacionespecifica:
            contador_especifico+=1
    print(f"Hay un total de {contador_especifico} en tus notas")
else:
    print("No se requiere comparacion")




#nullpointexception revisar esta excepcion 


    

