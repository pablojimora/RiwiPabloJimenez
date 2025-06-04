library={'mercedes': ['pablo', 'comedia', '2010', 50, 50000.0],'carota': ['caro', 'miedo', '2040', 100, 40000.0]}

def book_append(title:str,author:str,genre:str,year_publication:int,quantity:int,price_replacement:float):
    books=[]
    books.append(author)
    books.append(genre)
    books.append(year_publication)
    books.append(quantity)
    books.append(price_replacement)
    library[title]=books
    print("The book was entered successfully")
def search_books(title):
    print(library[title])
def update_books(title,quantity,price_replacement):
    librarylist:list=list(library[title])
    librarylist[3]=(quantity)
    librarylist[4]=(price_replacement)
    library[title]=tuple(librarylist)
    print("The book was updated")
def delete_books(title,quantityToDelete):
    librarylist:list=list(library[title])
    newquantity= librarylist[3] - int(quantityToDelete)
    librarylist[3]=newquantity
    library[title]=tuple(librarylist)
    print("The books was deleted")


enter_to_library:str=str(input("Do you want to enter to library?(yes/no): "))

while enter_to_library == "yes":
    print("1. Input book")
    print("2. Search books")
    print("3. Update books")
    print("4. Delete books")
    print("5. Generate reports")


    option:str=str(input("What option would you like to do?: "))
    if option == "1":
        enterbooktest:str=str(input("Do you want to input a book?(yes/no): "))
        if enterbooktest == "yes":
            title:str=str(input("Input the title of the book: "))
            author:str=str(input("Input the author's name: "))
            genre:str=str(input("Input the genre's book: "))
            year_publication:str=str(input("Input the year of publication of the book:"))
            quantity:int=int(input("Input the book's quantity: "))
            price_replacement:float=float(input("Input the price of the book: "))
        else:
            continue

        book_append(title,author,genre,year_publication,quantity,price_replacement)


    if option == "2":
        searchbooks:str=str(input("Do you want to search a book?(yes/no): "))
        if searchbooks == "yes":
            title:str=str(input("What book do you search?: "))
            search_books(title)
        else:
            continue
    #IMPORTANTE
    # if option == "3":
    #     updatePriceQuantity:str=str(input("Do you want to update information?(yes/no): "))
    #     if updatePriceQuantity == "yes":
    #         title:str=str(input("Input the title of the book that you want to update?: "))
    #         if title in library.keys():
    #             while True:

    #                 try:
    #                     price:float=float(input("Input the price to update: "))
    #                     quantity:float=float(input("Input the quantity to update: "))
    #                     break
    #                 except ValueError:
    #                     print("Input a valid value in price and quantity")
    #                     continue
    #             update_books(title,quantity,price)
    #         else:
    #             print("The book doesn't find in the library")
    #             continue
    #     else: 
    #         continue
    
    if option == "4":
        deletebooks:str=str(input("Do you want delete any book?(yes/no): "))
        if deletebooks == "yes":
            title:str=str(input("Input the title to delete: "))
            if title in library.keys():
                quantityToDelete:int=int(input("How much books do you want delete?: "))
                if quantityToDelete>library[title][3]:
                    print("You can't delete that books, because the quantity is bigger than quantity entered")
                else:
                    confirmationdelete:str=str(input("Are you sure delete this books?(yes/no): "))
                    if confirmationdelete == "yes":
                        delete_books(title,quantityToDelete)
                    else:
                        continue
            else:
                print("This book isn't in the library")
                continue    
    
    if option == "5":
        print("1. Calculate the total value of the inventory")
        print("2. Show the oldest and most recent book by genre")
        optiongenerate:str=str(input("What report would you like to do?: "))
        if optiongenerate == "1":
            inventory:list=list(library.values())
            totalvalue=sum(map(lambda i:i[3]*i[4], inventory))
            print(f"The total value of the inventory is {totalvalue}")
        elif optiongenerate == "2":
            print("Hacer lo de los libros")
        else: 
            continue
    print(library)


