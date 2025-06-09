from clase_especialidad import Especialidad

class Medico:
    def __init__ (self, nombre: str, matricula: str, especialidades: list[Especialidad]): 
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if especialidad.atiende_el_dia(dia):
                return especialidad.nombre
        return None

    def __str__(self):
        especialidades_str = "; ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, Matrícula: {self.__matricula}, Especialidades: [{especialidades_str}]"


