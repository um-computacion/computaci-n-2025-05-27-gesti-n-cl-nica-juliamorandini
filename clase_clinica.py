from clase_paciente import Paciente
from clase_medico import Medico
from clase_turno import Turno
from clase_receta import Receta
from clase_historia_clinica import Historia_clinica

from datetime import datetime
class PacienteNoEncontradoException(Exception):
    pass

class MedicoNoDisponibleException(Exception):
    pass

class TurnoOcupadoException(Exception):
    pass

class RecetaInvalidaException(Exception):
    pass

class Clinica:
    def __init__(self, pacientes: dict[str, Paciente], medicos: dict[str, Medico], turnos: list[Turno], histroria_clinica: dict[str, Historia_clinica]):
        self.pacientes = pacientes
        self.medicos = medicos
        self.turnos = turnos
        self.histroria_clinica = histroria_clinica
        #perdon por tantos commits :)