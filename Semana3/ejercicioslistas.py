# #Ejercicio 1
lista1=[1,2,3,4,5]
suma=0
for i in lista1:
    suma= i+suma
print(suma)
#Ejercicio 2
lista=[1,2,2,3,4,4,5]
listadepurada=[]
def depurar_lista():
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
    print(lista)
depurar_lista()
#Ejercicio 3

lista=[10,20,30,40]
listareversa=[]
for i in range(len(lista)-1,-1,-1):
    listareversa.append(lista[i])
print(listareversa)

#ejercicio4 contador de palabras
lista=("hola","mundo","hola","python")
contador=0
diccionario={}
for i in lista:
    diccionario[i]=lista.count(i)
print(diccionario)

#ejercicio 5 combinar dos listas 
lista1=[1,3,5] 
lista2=[2,4,6]

listafinal=lista1+lista2
print(sorted(listafinal))

#ejercicio6 mayor y menor
tupla=(5,2,9,1,7)
print(max(tupla),min(tupla))

#ejecicio 7 desempaqeuatdo de tuplas
tupla=(3,5,7,9)



                

       

    