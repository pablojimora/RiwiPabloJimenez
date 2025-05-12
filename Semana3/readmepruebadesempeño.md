### PRUEBA DE DESEMPEÑO
<p>
Esta es la prueba de desempeño número 1 del lenguaje de programación de alto nivel Python, la cual fue solicitada por Riwi,  y realizada por Pablo Jiménez Mora.
El manejo del inventario tiene las siguientes funcionalidades: 
</p>

#### Funciones del proyecto
<p>
Como requerimiento habían diferentes funciones que debía realizar el programa, las cuales, están implementadas dentro de un menú interactivo para el usuario, que por medio de números puede hacer su elección de la acción que quiera realizar con el inventario.  Estas funciones son:
</p>

-**Opción 1: Agregar productos al inventario**
Esta función como su nombre lo indica, es para añadir productos al inventario, primeramente te va a preguntar, cuántos productos quieres agregar, para así proseguir a pedirte la información de cada uno de ellos, cuando termines de digitar la información, te aparecerá este mensaje de confirmación "The product is entered succesfully", el cual confirma que los productos que ingresaste fueron cargados correctamente al inventario. 

 El precio y la cantidad, deben de ser valores válidos, siendo números positivos, y no pueden contener letras, ni símbolos que eviten un buen procesamiento de los datos, en caso tal de que estas reglas no sean cumplidas va a imprimir este mensaje "The values are invalid, please try again.", y te va a volver a permitir ingresar los valores de nuevo. 
  
  Por último va a mostrar tu inventario, luego de haber ingresado los productos, para que puedas revisar que todo quede bien.

  ```
 ej: Entrada:
  * How many products do you enter firstly?:  1
  * Enter the name of the product 1: platano
  *Enter the price of the product:  700
  * Enter the quantity of the product: 1000

   Salida: 
   * 'platano': (700.0, 1000)
Funcion:  

def products_append(nameProduct:str,price:float,quantity:int):
    product=[]
    product.append(price)
    product.append(quantity)
    product=tuple(product)
 #With this line, I declare that the product name is the dictionary key, and I assign the price and quantity, which are in the product tuple.
    inventory[nameProduct]=product
```

- **Opción 2: Buscar productos**
 Esta sencilla función te va a permitir visualizar todos los productos que tengas ingresados, para que así puedas elegir uno, escribir su nombre, y que te muestre, los datos de nombre, precio y cantidad que tengas disponible en tu inventario.
```
ej: Entrada:
 * What product do you need to search?: platano
 Salida: 
 * The product platano have a price of: 700, and a quantity of 1000
Funcion:

def search_products(nameProduct:str):
    print(f" The product {nameProduct}: have a price of: {inventory[nameProduct][0]}, and a quantity of: {inventory[nameProduct][1]}")
```

- **Opción 3: Actualizar productos**
 Esta función te permite actualizar tu inventario, ya sea porque necesites cambiar el precio de tus productos, o porque hayas recibido o vendido mercancía, y debas actualizar su cantidad.
```
 ej: Entrada:
 * What product do you want to udpate?:  platano
 * Enter the new price of the product: 1000
 * Enter the new quantity of the product: 500
 Salida:
 * platano': (1000.0, 500)
 * The values were updated

Funcion:

def update_products(nameProduct:str,price:float,quantity:int):
    inventory[nameProduct]=(float(price),float(quantity))
```

- **Opción 4: Eliminar productos**
Esta función te permite eliminar productos que ya vayas a sacar de comercialización en tu tienda, lo unico que debes hacer es ingresar el nombre del producto, luego de esto, tendrás que confirmar si de verdad estás seguro de eliminar el prodcuto, con la palabra clave "yes", si es así, en caso de que no lo devolverá al inicio del menú para elegir la opción que quiera realizar. El programa válida con anterioridad si el prodcuto ingresado está en el inventario, 
en caso de que no, sucederá lo mismo,  mostrará este mensaje "This product isn't in the inventory", y volverás al menú de opciones.
```
ej: Entrada:
* What product do you want to delete?:  platano
* Are you sure to delete this product?(yes/no):  yes

Salida: 
*The product was eliminated
*imprime el inventario sin el producto, ya que fue eliminado

Funcion:

def delete_products(nameProduct:str):
    del(inventory[nameProduct])
```


- **Opción 5: Calcular inventario**
 Esta opción es muy útil, ya que te genera el valor total de todo tu inventario para así poder llevar la contabilidad de lo que tienes en tu negocio. Siempre va a salir el valor con dos cifras decimales.
```

 ej: Entrada: 
 * "Do you want to calculate the total value of the inventory?(yes/no): yes
 Salida: 
 * The total value of the inventory is {el valor total del inventario con dos decimales}")

Funcion:

def calculate_total_value():
    products=list(inventory.values())
    totalvalue=sum(map(lambda i:i[0]*i[1],products))
    print(f"The total value of the inventory is {totalvalue:.2f}")
```

- **Opción 6: Salir del sistema**
En caso de que ya no necesites realizar ninguna opción, te recomiendo salir del sistema para así evitar cualquier cambio indeseado. 
 

