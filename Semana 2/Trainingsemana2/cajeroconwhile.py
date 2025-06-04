opcion:int=int(input("Oprima 1 si quiere ingresar a las funciones del cajero"))
saldo=1000000
while opcion == 1:
    print("Con 1 puede ver su saldo")
    print("COn 2 puede depositar dinero")
    print("Con 3 puede retirar dinero")
    print("Una opcion diferente hace que salga del programa")
    opciondentrodelcajero=int(input("Ingrese la operacion que quiera realizar"))

    if opciondentrodelcajero == 1:
        print(f"Su saldo es de {saldo}")
    elif opciondentrodelcajero == 2:
        deposito:float=float(input("Ingrese el valor que va a depositar"))
        saldo=deposito+saldo
        print(f"Su saldo luego del deposito es de {saldo}")
    elif opciondentrodelcajero == 3:
        retiro:float=float(input("Cuanto dinero desea retirar"))
        if retiro > saldo:
            print("El valor excede su saldo")
        else:
            print("Retiro exitoso")
            saldo=saldo - retiro
            print(f"Su saldo final despues del reitiro es de {saldo}")

    break
