from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
from datetime import datetime
class Receta :
    def __init__ (self, paciente: Paciente, medico: Medico, medicamentos: list[str], fecha: datetime):
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.fecha = fecha
    

    def __str__(self):
        medicamentos_str = "[" + ", ".join(self.__medicamentos) + "]"
        paciente_str = str(self.__paciente)
        medico_str = str(self.__medico).replace("\n", "\n    ")
        return (f"Receta(\n"
                f"  Paciente({paciente_str}),\n"
                f"  Medico(\n    {medico_str}\n  ),\n"
                f"  {medicamentos_str},\n"
                f"  {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n")