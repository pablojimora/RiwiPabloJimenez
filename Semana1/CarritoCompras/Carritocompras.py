print("Registra 5 productos")
#Producto 1
print("Producto 1: ")
nombre=input("Ingrese el nombre del producto ")
precio_unitario=float(input("Ingrese el valor del producto "))
cantidad=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario > 0 and cantidad > 0:
    print("Valores válidos")
else:
    print("Los valores introducidos son inválidos")
total1=cantidad*precio_unitario

#Producto 2
print("Producto 2: ")
nombre2=input("Ingrese el nombre del producto ")
precio_unitario2=float(input("Ingrese el valor del producto "))
cantidad2=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario2> 0 and cantidad2 > 0:
    print("Valores válidos")
else:
    print("Los valores introducidos son inválidos")

total2=cantidad2*precio_unitario2

#Producto 3
print("Producto 3: ")
nombre3=input("Ingrese el nombre del producto ")
precio_unitario3=float(input("Ingrese el valor del producto "))
cantidad3=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario3> 0 and cantidad3 > 0:
    print("Valores válidos")
else:
    print("Los valores introducidos son inválidos")

total3=cantidad3*precio_unitario3

#Producto 4
print("Producto 4: ")
nombre4=input("Ingrese el nombre del producto ")
precio_unitario4=float(input("Ingrese el valor del producto "))
cantidad4=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario4> 0 and cantidad4 > 0:
    print("Valores válidos")
else:
    print("Los valores introducidos son inválidos")

total4=cantidad4*precio_unitario4

#Producto 5
print("Producto 5: ")
nombre5=input("Ingrese el nombre del producto ")
precio_unitario5=float(input("Ingrese el valor del producto "))
cantidad5=int(input("Ingrese la cantidad del producto que se va a adquirir "))
#Con este condicional se verifica si el precio unitario o la cantidad sean numeros positivos
#En caso tal de no serlos se devuelve el mensaje 
if precio_unitario5> 0 and cantidad5 > 0:
    print("Valores válidos")
else:
    print("Los valores introducidos son inválidos")

total5=cantidad5*precio_unitario5

#total de los 5 productos
total=total1+total2+total3+total4+total5
print("                         Subtotal                               ")
print(f"Producto 1: {nombre}, cantidad: {cantidad}, subtotal: {total1}")
print(f"Producto 2: {nombre2}, cantidad: {cantidad2}, subtotal: {total2}")
print(f"Producto 3: {nombre3}, cantidad: {cantidad3}, subtotal: {total3}")
print(f"Producto 4: {nombre4}, cantidad: {cantidad4}, subtotal: {total4}")
print(f"Producto 5: {nombre5}, cantidad: {cantidad5}, subtotal: {total5}")
#total final
print(f"El valor total de su compra es de {total}")

if total < 50000:
    print(f"Nuestro método de pago sugerido es EFECTIVO ")
    print("Por realizar su pago con el método sugerido, usted tendrá un 5% de descuento")
    total_con5= total -(total*0.05)
    print(f"El valor con este descuento es de {total_con5}")
elif total >= 50000 and total <= 100000:
    print(f"Nuestro método de pago sugerido es TARJETA")
    print("No tiene ningún beneficio")
else:
    print(f"Nuestro método de pago sugerido es TRANSFERENCIA")
    print("Por realizar su pago con el método sugerido, usted tendrá un 2% de cashback")
    cashback= total * 0.02
    print(f"El valor de su cashback es de {cashback}")