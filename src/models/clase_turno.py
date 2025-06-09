from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
import datetime

class Turno:
    def __init__(self, paciente = None, medico = None, fecha_hora: datetime.datetime = None, especialidad: str = None):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora
    
    def __str__(self):
        return f"Turno:\n  Paciente: {self.__paciente}\n  Médico: {self.__medico}\n  Especialidad: {self.__especialidad}\n  Fecha y hora: {self.__fecha_hora}"