print("Bienvenido al mercadona")
print("Para nosotros es un gusto atenderlo el dia de hoy")
print("Mi nombre es Riwibot, y mi función consiste en")
print("Realizar la consulta del valor de sy producto")
print("Recuerda los descuentos que tenemos por cada dia de la semana")
print("Lunes: Lácteos")
print("Martes: Carnes")
print("Miercoles: Licores")
print("Jueves: Aseo")
print("Viernes: Loncheras")
print("Sábados: descuentos sorpresa")
print("Domingos: descuentos sorpresa")
print("Por favor")

#Lineas para pedir a los usuarios los primeros datos
nombre=input("Ingrese el nombre del producto ")
precio_unitario=float(input("Ingrese el valor del producto "))
cantidad=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario > 0 and cantidad > 0:
    print("Valores válidos")
    descuento=(input("¿El producto tiene descuento?(SI/NO) "))
#Esta linea valida si el precio tiene descuento, en caso tal de que si, se realiza las operaciones pertinentes para realizar los precios solicitados
    if descuento == "SI":
        valor_descuento=int(input("¿Cuanto es el descuento aplicado? "))
        if valor_descuento > 0 and valor_descuento <= 100: 
            cuenta= precio_unitario * cantidad
            cuenta_descuento =  cuenta - (cuenta*valor_descuento/100)
            print(f"El producto {nombre}, tiene un precio sin descuento de {cuenta:.2f}")
            print(f"Aplicando el descuento, el producto {nombre}, queda con un precio de {cuenta_descuento:.2f}")
        else: 
            print("EL valor del descuento es inválido")
    #En caso tal de que no haya descuento realiza el calculo del precio sin descuento        
    else:
        cuenta_sindescuento= precio_unitario * cantidad
        print(f"El producto {nombre}, tiene un valor de {cuenta_sindescuento:.2f}")
        print("En fechas proximas se vendrán muchos descuentos para diferentes productos")
else:
    print("Los valores introducidos son inválidos")