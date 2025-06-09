from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
from datetime import datetime

class Receta:
    def __init__(self, paciente = None, medico = None, medicamentos: list = None, fecha: datetime = None):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos if medicamentos is not None else []
        self.__fecha = fecha

    def __str__(self):
        medicamentos_str = "[" + ", ".join(self.__medicamentos) + "]"
        paciente_str = str(self.__paciente)
        medico_str = str(self.__medico).replace("\n", "\n    ")
        return (f"Receta(\n"
                f"  Paciente({paciente_str}),\n"
                f"  Medico(\n    {medico_str}\n  ),\n"
                f"  {medicamentos_str},\n"
                f"  {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n")