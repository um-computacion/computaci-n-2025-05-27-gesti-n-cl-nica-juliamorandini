from clase_paciente import Paciente
from clase_receta import Receta
from clase_turno import Turno
class Historia_clinica:
    def __init__(self, paciente: Paciente, turnos: list[Turno], recetas: list[Receta]):
        self.paciente = paciente
        self.turnos = turnos
        self.recetas = recetas

    def agregar_turnos(self, turnos: Turno):
        self.turnos.append(turnos)

    def obtener_turnos(self):
        return list(self.turnos)
    
    def obtener_recetas(self):
        return list(self.recetas) #me dice que no detecta el self?
    
    def __str__(self):
        turnos_str = "\n    ".join(str(t) for t in self.__turnos)
        recetas_str = "\n    ".join(str(r) for r in self.__recetas)
        return (f"HistoriaClinica(\n"
                f"  Paciente: {self.__paciente}\n"
                f"  Turnos:\n    {turnos_str if turnos_str else 'Sin turnos'}\n"
                f"  Recetas:\n    {recetas_str if recetas_str else 'Sin recetas'}\n"
                f")")