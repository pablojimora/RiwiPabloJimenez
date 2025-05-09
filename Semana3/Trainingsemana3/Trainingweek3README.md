### PROYECTO SEMANA 3, INVENTARIO
<p>
Este programa es el entrenamiento de la semana 3 de mi desarrollo como coder en la empresa Riwi, el cual fue solicitado por ellos, para verificar el manejo de los temas aprendidos a lo largo del tiempo que he entrenado con ellos, guiado y asesorado principalmente por mi team leader Pedro.
</p>

#### Funciones del proyecto
<p>
Como requerimiento habían diferentes funciones que debía realizar el programa, las cuales, están implementadas dentro de un menú interactivo para el usuario, que por medio de números puede hacer su elección de la acción que quiera realizar con el inventario.  Estas funciones son:
</p>

-**Opción 1: Agregar productos al inventario**
Se debe insertar el nombre, precio y la cantidad que se maneje del producto que se vaya a añadir, ten en cuenta que si añades un producto con el mismo nombre en el inventario, el programa no te lo va a permitir para así evitar la duplicación de información. 

```
def products_append(name:str,price:float,quantity:int):
    product=[]
    product.append(price)
    product.append(quantity)
    product=tuple(product)
    #With this line, i said to append the product list, to product name, it would be the "key"
    products[name]=product
```

- **Opción 2: Buscar productos**
Esta función solo necesita el nombre del producto, para que luego de insertarlo, te muestre su precio, y luego su cantidad respectivamente.

```
def search_product(name:str):
    #with this condition i check if the name products belong to the dictionary keys, if it's true, print it's information
    if name in products.keys():
        print(products[name])
    else:
        print("The product doesn't find in the inventory")
```

- **Opción 3: Actualizar productos**
Esta función utiliza el nombre del producto para poder seleccionar la información que quieras actualizar, primero te pedirá el nuevo precio, luego que actualices la cantidad de producto que tengas.
 
```
def update_product(name:str,price:float,quantity:int):
    products[name]=(float(price),float(quantity))
    print("The price and quantity were updated")
```

- **Opción 4: Eliminar productos**
Debes insertar el nombre del producto que desees eliminar. luego de esto, te muestra cual producto has eliminado, no te preocupes, en caso de eliminar algo por error, puedes volver a añadirlo con la opción 1.

```
def delete_product(name:str):
    del(products[name])
    print(f"The product {name} was eliminated successfuly")
```


- **Opción 5: Calcular inventario**
Por último, se puede calcular el valor total de todos los productos que tengas en el inventario, para así poder llevar la contabilidad de una mejor forma. 

```
def calculate_value_inventory():
    inventory=list(products.values())
    valortotal=sum(map(lambda i:i[0]*i[1], inventory))
    print(f"The total of inventory is {valortotal}")
```

- **Opción 6: Salir del sistema**
En caso de que ya no necesites realizar ninguna opción, te recomiendo salir del sistema para así evitar cualquier cambio indeseado. 
