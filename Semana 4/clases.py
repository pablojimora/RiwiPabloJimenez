class Humano:
    def __init__(self,nombre:str,apellido:str,cedula:int):
        self.nombre=nombre
        self.apellido=apellido 
        self.cedula=cedula
    
class Datos(Humano):
    def __init__(self,nombre:str,apellido:str,cedula:int,carrera:str):
        super().__init__(nombre,apellido,cedula)
        self.carrera=carrera

    def informacion(self):
        print(f"El estudiante {self.nombre} {self.apellido}, con cedula {self.cedula}, esta estudiando {self.carrera}")

datos= Datos("Pablo","Jimenez",1000549308,"Ing biomedica")
Datos.informacion(datos)
