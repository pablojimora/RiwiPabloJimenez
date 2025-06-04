class Persona:
    def __init__(self,nombre:str,edad:int,direccion:str):
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años, y vivo en {self.direccion}")

persona1=Persona("Pablo",24,"Cra 88 #31e-35")
persona2=Persona("Carolina",22,"Calle 4 sur #48-110")

persona1.saludar()
persona2.saludar()