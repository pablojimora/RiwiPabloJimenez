from datetime import datetime,date,time
import csv

flights:str={
"AV-101": {
"origen": "lima",
"destino": "bogotá",
"asientos": ["A1", "A2", "B1", "B2"],
"horario": (14, 30),
"fecha": (2025,5,16)},
"AV-102": {
"origen": "medellín",
"destino": "bogotá",
"asientos": ["A1", "A2", "B1", "B2"],
"horario": (15, 30),
"fecha": (2025,5,16)},
"AV-103": {
"origen": "cali",
"destino": "bogotá",
"asientos": ["A1", "A2", "B1", "B2"],
"horario": (16, 30),
"fecha": (2025,5,16)}
}

def seat_reservation(origen,destino):
    for nombre, vuelos in flights.items():
        if vuelos['origen']==origen and vuelos['destino']==destino:
            print (f"El avion {nombre} tiene los siguientes asientos disponibles {vuelos['asientos']}")
            asiento:str=str(input("Cual asiento desea reservar?"))
            if asiento in vuelos['asientos']:
                vuelos['asientos'].remove(asiento)
                print("Su asiento fue reservado con exito")
                print(vuelos['asientos'])
        else:
            print("El vuelo no se ha encontrado")
            return
def ocupacion_flight(vuelo):
    for nombre, vuelos in flights.items():
        capacidad=50
        if nombre == vuelo:
            capacidadporcentaje=(len(vuelos['asientos'])/capacidad)*100
            print(f"EL vuelo tiene un {capacidadporcentaje} % de capacidad disponible")
        else: 
            print("El vuelo no se ha encontrado") 
            return
def gen_text():
    newlist=[]
    for x,y in flights.items():
        l1=[x]
        l1.extend(list(y.values()))
        hora=time(l1[4][0],l1[4][1])
        l1[4]=hora
        newlist.append(l1)
    newlist.sort(key=lambda x: x[4])
    with open('reporte.txt','a') as archive:
        for nline in newlist:
            line = f'Flight: {nline[0]}, Origin: {nline[1]}, Destination: {nline[2]}, Seats: {','.join(nline[3])}, Time: {nline[4]}\n'
            print(line)
            archive.write(line)
            


optionmenu:str=str(input("Quiere ingresar a la opcion?(yes/no): ").lower())

while optionmenu == "yes":
    print("1. Seat reservation")
    print("2. Ocupation")
    print("3. Generate report")
    print("4. Exit")

    option:int=int(input("What option do you want to do?: "))
    if option == 1:
        origin:str=str(input("What is the travel's origin ?: ").lower())
        destiny:str=str(input("What is the travel's destiny?: ").lower())
        seat_reservation(origin,destiny)
    elif option == 2:
        flight:str=str(input("What is your flight?: "))
        ocupacion_flight(flight)
    elif option == 3:
        gen_text()
    elif option == 4:
        exitconfirmation:str=str(input("Do you want to exit?(yes/no): ").lower())
        if exitconfirmation == "yes":
            break
        else:
            continue
    else:
        print("This option doesn't exist")
        continue
