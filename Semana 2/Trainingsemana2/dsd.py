
contar_mayor:str=str(input("Desea contar calificaciones mayores a alguna calificacion?(si/no)"))
contar_especifica:str=str(input("Desea contar alguna calificacion en especifico?(si/no)"))
sumar:int=0
contador_mayor:int=0
contador_especifico:int=0
incrementador:int=0
notasstr:str=""
texto4:str=""
#Listas
notas:list[float]=[]
valor_mayor_a:list[float]=[]

#Este ciclo for es el encargado de pedir la cantidad de notas que diga el usuario, validar si estan aprobadas o no, y añadirlas a la lista notas
notasstr=input("Ingrese sus notas separadas por comas, las calificaciones son de 0 a 100: ")
for i in notasstr:
    if i != ",":
       texto4 = texto4. __add__(i)
    else:
        numero:float = float(texto4)
        texto4=""
        sumar=sumar+numero
        notas.append(numero)
#Esta variable sirve para guardar la     
    contadorPosicion=len(notasstr)-1
    if contadorPosicion == incrementador:
        numero:float = float(texto4)
        texto4=""
        sumar=sumar+numero
        notas.append(numero)
    incrementador+=1
print(notas)
print(len(notasstr))
