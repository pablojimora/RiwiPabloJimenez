#Programa que me valide una conexion a una base de datos, que me valide nombre de la base de datos, usuario, contraseña y el puerto
nombre= "dbriwi"
usuario= "pablojimora"
contraseña="Riwi2025*"
puerto="3080"
url="www.riwi.com/BD"

urlfinal= nombre+"/"+usuario+"/"+contraseña+"/"+puerto+"/"+url

nombredb=input("Ingrese el nombre de la base de datos ")
usuariodb=input("Ingrese su usuario ")
contraseñadb=input("Ingrese su contraseña ")
puertodb=(input("Ingrese el numero de puerto "))
urldb=input("Ingrese la url de la DB ")

urlingresada=nombredb+"/"+usuario+"/"+contraseñadb+"/"+puertodb+"/"+urldb

if urlfinal == urlingresada:
    print("Ingreso a la base de datos completado con exito")
    print(f"Bienvenido {usuario} a la base de datos {nombre}")
    print(f"Los datos ingresados fueron {urlfinal}")

else:
    print("Algún dato ingresado contiene errores")

