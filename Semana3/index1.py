libros = {}
ID = 1

def agregar_libro():
    global ID
    while True :
        titulo = input ("introduce el nombre de la obra: ")
        autor = input ("introduce el nombre del autor: ")
        año = input ("introduce el año de lanzamiento: ")
        if año.isdigit():
            ID2 = f"{ID:03d}"
            libros2 = {
                'Titulo': titulo,
                'Autor': autor,
                'Año': int(año)
            }
            ID += 1
            libros[f"ID {ID2}"] = libros2
            print ("\nlibro agregado exitosamente")
            titulo2 = (f"{ID2}: Titulo: {titulo}, Autor: {autor}, Año de lanzamiento: {año}")
            print (titulo2)
    
            break
        else:
            print ("Solo se pueden introducir numeros")

def mostrar_libros():
    for id, elementos in libros.items():
        print(f"{id}: Titulo: {elementos['Titulo']}, Autor: {elementos['Autor']}, Año de lanzamiento: {elementos['Año']}")

def busqueda():
    while True:
        busqu3da = input ("introduce el ID o titulo de la obra: ").lower()
        id = "ID " + busqu3da
        if id in libros:
                libro = libros(id)
                print (f"Libro encontrado: {id}, Titulo: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Año']}")
                break
        else:
            print("Libro no encontrado.")
            
while True:
    print ("\n1. Agregar un libro")
    print ("2. mostrar libros")
    print ("3. buscar libros")
    resp2 = input ("\nBienvenido a la biblioteca, selecciona la acción que desees realizar: ")

    if resp2 == "1":
        agregar_libro()
    if resp2 == "2":
        mostrar_libros()
    if resp2 == "3":
        busqueda()