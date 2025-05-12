inventory:dict={'leche': (1000.0, 10), 
                'carne': (1000.0, 10), 
                'huevos': (1000.0, 10), 
                'platano': (1500.0, 80), 
                'mango': (1000.0, 10)}
#With this function i append a new products in the dictionary, first I add them to a list and then convert them into a tuple.
def products_append(nameProduct:str,price:float,quantity:int):
    product=[]
    product.append(price)
    product.append(quantity)
    product=tuple(product)
 #With this line, I declare that the product name is the dictionary key, and I assign the price and quantity, which are in the product tuple.
    inventory[nameProduct]=product
#With this line, i print the name, price and quantity of the product that searched the user
def search_products(nameProduct:str):
    print(f" The product {nameProduct} have a price of: {inventory[nameProduct][0]}, and a quantity of: {inventory[nameProduct][1]}")
#With this function, i change the values of product selected, to the new values
def update_products(nameProduct:str,price:float,quantity:int):
    inventory[nameProduct]=(float(price),float(quantity))
#with this function, i delete the product, deleting the key of dictionary inventory, in addition deleting the other information
def delete_products(nameProduct:str):
    del(inventory[nameProduct])
#With this line i used the function map, and lamda to iterate all of prices, and all of quantities, and multiplicate them later sum, and get up the total value
def calculate_total_value():
    products=list(inventory.values())
    totalvalue=sum(map(lambda i:i[0]*i[1],products))
    print(f"The total value of the inventory is {totalvalue:.2f}")


#I used a while loop to make the menu, the user can choose a option to make in the inventory
#In each inputs i used, try and except to handle possible value error
#I used conditionals for valid the values entered were correct according to the instruccions
optionEnterInventory:str=str(input("Do you want enter to inventory?(yes/no): ").lower())
while optionEnterInventory == "yes":
    try:
        print("1. Enter products")
        print("2. Search products")
        print("3. Update products")
        print("4. Delete products")
        print("5. Calculate total value of inventory")
        print("6. Exit of the inventory")

        option:int=int(input("What option do you want to do?: "))
        if option == 1:
            appendtest:str=str(input("Do you want to append a product(yes/no): ").lower())
            if appendtest == "yes":
                quantityproduct:int=int(input("How many products do you enter firstly?: "))
                for i in range(quantityproduct):
                    nameProduct:str=str(input(f"Enter the name of the product {i+1}: ").lower())
                    if nameProduct in inventory.keys():
                        print("The product is in the inventory, please enter a new product.")
                    else:
                        while True:
                            try: 
                                price:float=float(input("Enter the price of the product: "))
                                quantity:int=int(input("Enter the quantity of the product: "))
                                products_append(nameProduct,price,quantity)
                                print("The product is entered succesfully")
                                print(inventory)
                                break
                            except ValueError:
                                print("The values are invalid, please try again.")
                                continue
                continue
                                
            else:
                continue
        if option == 2:
            searchtest:str=str(input("Do you want to search a product?(yes/no): ").lower())
            if searchtest == "yes":
                print(inventory.keys())
                productToSearch:str=str(input("What product do you need to search?: ").lower())
                if productToSearch in inventory.keys():
                    search_products(productToSearch)
                else:
                    print("This product isn't in the inventory")
                    continue
                continue
            else: 
                continue
        if option == 3:
            updatetest:str=str(input("Do you want to update a product?:(yes/no): ").lower())
            if updatetest == "yes":
                updateProduct:str=str(input("What product do you want to udpate?: ").lower())
                if updateProduct in inventory.keys():
                    while True:
                        try:
                            price:float=float(input("Enter the new price of the product: "))
                            quantity:int=int(input("Enter the new quantity of the product:"))
                            if price > 0 and quantity > 0:
                                update_products(updateProduct,price,quantity)
                                print("The values were updated")
                                print(inventory)
                                break
                            else:
                                print("The price or the quantity are incorrect, please check the values")
                            continue
                        except ValueError:
                            print("Enter the valid products, please try again")
                            continue
                    continue
                else:
                    print("This product isn't in the inventory")
                    continue
            else:
                continue
        if option == 4:
            deletetest:str=str(input("Do you want to delete a product(yes/no): ").lower())
            if deletetest == "yes":
                productToDelete:str=str(input("What product do you want to delete?: ").lower())
                if productToDelete in inventory.keys():
                    deleteconfirm:str=str(input("Are you sure to delete this product?(yes/no): ").lower())
                    if deleteconfirm == "yes":
                        delete_products(productToDelete)
                        print("The product was eliminated")
                        print(inventory)
                        continue
                    else:
                        continue
                else:
                    print("This product isn't in the inventory")
                    continue
            else: 
                continue
        if option == 5:
            calculatetest:str=str(input("Do you want to calculate the total value of the inventory?(yes/no): ").lower())
            if calculatetest == "yes":
                calculate_total_value()
                continue
            else:
                continue
        if option == 6:
            exittest:str=str(input("Are you sure to exit of the inventory?(yes/no): ").lower())
            if exittest == "yes":
                break
            else:
                continue
        break
    except ValueError:
        print("Enter a valid valid please")
        continue            
            
                    



