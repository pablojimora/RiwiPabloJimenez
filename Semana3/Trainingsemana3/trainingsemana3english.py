products={'leche': (400.0, 4),
          'sardina': (300.0, 3),
          'manzana': (200.0, 6)
          }

def products_append(name:str,price:float,quantity:int):
    product=[]
    product.append(price)
    product.append(quantity)
    product=tuple(product)
    #With this line, i said to append the product list, to product name, it would be the "key"
    products[name]=product


def search_product(name:str):
    #with this condition i check if the name products belong to the dictionary keys, if it's true, print it's information
    if name in products.keys():
        print(products[name])
    else:
        print("The product doesn't find in the inventory")
    #With this function, i change the values of product selected, to the new values
def update_product(name:str,price:float,quantity:int):
    products[name]=(float(price),float(quantity))
    print("The price and quantity were updated")
    #with this function, i delete the product, deleting the key of dictionary products, in addition deleting the other information
def delete_product(name:str):
    del(products[name])
    print(f"The product {name} was eliminated successfuly")
    #With this function, i calculate total money of inventory, using lambda function, and map function , lambda being a map parameter, which says to
    #iterate in each inventory value of position 0, and multiplies it eith those of position 1.
def calculate_value_inventory():
    inventory:list=list(products.values())
    valortotal=sum(map(lambda i:i[0]*i[1], inventory))
    print(f"The total of inventory is {valortotal}")




enter_to_menu:str=str(input("Do you want to enter the inventory?(yes/no): "))


 #With this while loop, it allows you to have a menu of options for the user, each option is a function for an action in the library
while enter_to_menu == "yes":
    print("1. Input product")
    print("2. Search product")
    print("3. Update prices and quantities")
    print("4. Delete products")
    print("5. Calculate total money of inventory")
    print("6. Exit inventory")
    option=input("Enter the option you want to perform")
    if option == "1":
        producttest:str=input("Do you want to input a product?(yes/no): ")
        if producttest == "yes":
            name:str=(input("Input name product: "))
            if name in products:
                print("This product is already in the products.")
                continue
            price:float=(float(input("Input the price product: ")))
            quantity:int=(int(input("Input the quantity product: ")))
            products_append(name,price,quantity)
            print("The product was entered succesfully")
        else:
            continue
    elif option == "2":
        productSearch:str=input("Do you want to search for a product?(yes/no): ")
        if productSearch =="yes":
            nameproductSearch:str=input("Input the name product to search: ")
            search_product(nameproductSearch)
        else:
            continue
    elif option == "3":
        updateProduct:str=(input("Do you want to update a product? (yes/no): "))
        if updateProduct == "yes":
            name:str=input("Input the name product to update")
            price:float=input("Input the new price")
            quantity:int=input("Input the new quantity")
            if name in products.keys():
                update_product(name,price,quantity)
                print("The product was update successfully")
            else:
                print("The product wasn't in the inventory")
                continue
    elif option == "4":
        deleteProduct:str=str(input("Do you want to delete any product?(yes/no): "))
        if deleteProduct == "yes":
            name:str=input("Input the product to delete")
            if name in products.keys():
                delete_product(name)
                print("The product was deleted successfully")
            else:
                print("The product doesn't exist")
                continue
        else:
            continue
    elif option == "5":
        calculateInventory:str=input("Do you want to calculate the total value of the inventory?(yes/no): ")
        if calculateInventory == "yes":
            calculate_value_inventory()
        else: 
            continue
    elif option == "6":
        break
    #This print is to be able to view the products dictionary after making any changes
    print(products)

else:
    print("It wasn't possible to enter the inventory, please, try again")
