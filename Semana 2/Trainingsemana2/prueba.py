texto1:str =""
texto2:str =""
texto3:str=""
texto4:str=""
numero1:float=0.0
numero2:float=0.0
sumar:float =0
incrementador:int=0

texto1="mundo"
texto2="hola"

texto1="pedro"

print(f"{texto2} {texto1}")

texto1="2.5,45.3,80,100"
incrementador=0
for i in texto1:
    if i != ",":
       texto4 = texto4. __add__(i)
    else:
        numero:float = float(texto4)
        texto4=""
        sumar=sumar+numero
    contadorPosicion= len(texto1) -1

    if contadorPosicion == incrementador:
       numero:float = float(texto4)
       texto4=""
       sumar=sumar+numero 

    incrementador+=1
print(sumar)