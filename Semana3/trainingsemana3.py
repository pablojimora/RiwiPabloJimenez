products={'leche': [400.0, 4],
          'sardina': [300.0, 3],
          'manzana': [200.0, 6]
          }

def products_append(name:str,price:float,quantity:int):
    product=[]
    product.append(price)
    product.append(quantity)
    product=tuple(product)

    #Con esta linea le digo que le agregue la lista product,al nombre del producto, que seria la key 
    products[name]=product

def search_product(name:str):
    #Con este if reviso si el nombre de los productos pertenece a las llaves del diccionario, si si pertenece, imprime su infomracion
    if name in products.keys():
        print(products[name])
    else:
        print("El producto no se encuentra en el inventario")
    #Con esta funcion estoy seleccionando el producto por medio de la key, y luego actualizadno su perecio y cantidad
def update_product(name:str,price:float,quantity:int):
    products[name]=(float(price),float(quantity))
    print("El valor y la cantidad fueron actualizados")
    #Con est selecciona la key o sea el producto y lo elimina
def delete_product(name:str):
    del(products[name])
    print("El producto ha sido eliminado con exito")
    #Con este se realiza la suma de todos los precios del inventareio, recorriendo todas las posiciones "i", 
    #que seria cada producto, y luego la posicion 0, que es la cantidad y la 1 que es el precio

def calculate_value_inventory():
    inventory=list(products.values())
    #forma1
    valortotal=sum(map(lambda x:x[0]*x[1], inventory))
    print(valortotal)
    #forma 2
    # suma=0
    # for i in range(len(inventory)):
    #     multiplicacion=(inventory[i][0]*inventory[i][1])
    #     suma=multiplicacion+suma
    # print(suma)




enter_to_menu:str=input("Deseas ingresar al inventario?(si/no)")
print("1. Ingresar un producto")
print("2. Consultar un producto")
print("3. Actualizar precios")
print("4. Eliminar productos")
print("5. Calcular el valor total del inventario")
print("6. Salir del inventario")

#La forma de trabajo de este menu, se basa en que el usuario elija una opcion epende de la accin que quiera realizar, en cada una de las opciones, 
# ingrese por pantalla, los parametros que se necesiten segun la accion, y estos queden en el lenguaje de la funcion, para poder realizar la accion
#tambien validando con los condicionales, si cumple con las caracteristicas para realizar la accion con exito
while enter_to_menu == "si":
    option=input("Ingrese la opcion que quiera realizar")
    if option == "1":
        producttest:str=input("¿Deseas agregar un producto?(si/no)")
        if producttest == "si":
            name:str=(input("Ingrese el nombre del producto"))
            price:float=(float(input("Ingrese el precio del producto: ")))
            quantity:int=(int(input("Ingrese la cantidad del producto")))
            products_append(name,price,quantity)
            print("Fue ingresado exitosamente")
        else:
            continue
    elif option == "2":
        productSearch:str=input("Deseas consultar un producto?(si/no)")
        if productSearch =="si":
            nameproductSearch:str=input("Ingrese el nombre del producto a buscar")
            search_product(nameproductSearch)
        else:
            continue
    elif option == "3":
        updateProduct:str=(input("Desea actualizar algun producto? (si/no)"))
        if updateProduct == "si":
            name:str=input("Ingrese el producto que desee actualizar")
            price:float=input("Ingrese la actualizacion del precio")
            quantity:int=input("Ingrese la actualizacion de la cantidad")
            if name in products.keys():
                update_product(name,price,quantity)
                print("El producto ha sido actuliazado con éxito")
            else:
                print("El producto no está en el inventario")
                continue
    elif option == "4":
        deleteProduct:str=str(input("¿Desea eliminar algun producto?(si/no): "))
        if deleteProduct == "si":
            name:str=input("Ingrese el producto que desee eliminar")
            if name in products.keys():
                delete_product(name)
                print("EL producto fue eliminado correctamente")
            else:
                print("El producto no existe")
                continue
        else:
            continue
    elif option == "5":
        calculateInventory:str=input("¿Desea calcular el total del inventario?(si/no)")
        if calculateInventory == "si":
            calculate_value_inventory()
        else: 
            continue
    elif option == "6":
        break
    print(products)

else:
    print("No se logró ingresar, intentelo de nuevo")



