#El dos puntos es para definir desde el principio el tipo de variable que se va a utilizar
nota1:float=float(input("Ingrese su primera nota"))
nota2:float =float(input("Ingrese su segunda nota"))
nota3: float =float(input("Ingrese su tercera nota"))
promedio=(nota1+nota2+nota3)/3

if promedio >= 7:
    print("Promocionado")
elif promedio >=4:
    print("Regular")
else:
    print("Reprobado")