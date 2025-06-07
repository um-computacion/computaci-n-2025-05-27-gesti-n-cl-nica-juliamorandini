class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str): #constructor
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str: #getter
        return self.dni
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.dni}, {self.fecha_nacimiento}" #sigo aprendiendo a usar este tipo de formato 
    

    #sin setter xq la consigna no pide que se modifique el nombre 