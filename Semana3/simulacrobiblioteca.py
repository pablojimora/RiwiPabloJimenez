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



enter_to_library:str=str(input("Do you want to enter to library?(yes/no): "))

while enter_to_library == "yes":
    print("1. Input book")

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

    print(library)


