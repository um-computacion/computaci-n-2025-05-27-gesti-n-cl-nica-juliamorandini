from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
from src.models.clase_turno import Turno
from src.models.clase_receta import Receta
from src.models.clase_historia_clinica import Historia_clinica
from src.models.excepciones import (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException)

from datetime import datetime

class Clinica:
    def __init__(self, pacientes=None, medicos=None, turnos=None, historias_clinica=None):
        self.pacientes = pacientes if pacientes is not None else []
        self.medicos = medicos if medicos is not None else []
        self.turnos = turnos if turnos is not None else []
        self.historias_clinica = historias_clinica if historias_clinica is not None else {}
        

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"El paciente con DNI {dni} ya esta registrado")
        self.__pacientes[dni] = paciente
        self.__historias_clinica[dni] = Historia_clinica(paciente, [], [])

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"El medico con matrícula {matricula} ya esta registrado")
        self.__medicos[matricula] = medico


    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        return self.__medicos.get(matricula)

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)

    def obtener_historia_clinica(self, dni: str) -> Historia_clinica:
        return self.__historias_clinica.get(dni)



    #todo lo de turnos

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        if not self.validar_existencia_paciente(dni):
            raise PacienteNoEncontradoException("Paciente no registrado")
        if not self.validar_existencia_medico(matricula):
            raise MedicoNoDisponibleException("medico no registrado")

        medico = self.__medicos[matricula]
        paciente = self.__pacientes[dni]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)

        if not self.validar_turno_no_duplicado(matricula, fecha_hora):
            raise TurnoOcupadoException("El medico ya tiene un turno en ese horario")

        if not self.validar_especialidad_en_dia(medico, especialidad, dia_semana):
            raise MedicoNoDisponibleException("el medico no atiende esa especialidad ese dia")

        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinica[dni].agregar_turno(turno)



    # la parte de recetas

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        if not self.validar_existencia_paciente(dni):
            raise PacienteNoEncontradoException("Paciente no registrado.")
        if not self.validar_existencia_medico(matricula):
            raise MedicoNoDisponibleException("Médico no registrado.")
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento.")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)


    # validaciones
    def validar_existencia_paciente(self, dni: str) -> bool:
        return dni in self.__pacientes

    def validar_existencia_medico(self, matricula: str) -> bool:
        return matricula in self.__medicos

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime) -> bool:
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                return False
        return True

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str) -> bool:
        especialidad = medico.obtener_especialidad_para_dia(dia_semana)
        return especialidad == especialidad_solicitada




    def __str__(self):
        return f"Clínica con {len(self.__pacientes)} pacientes, {len(self.__medicos)} médicos y {len(self.__turnos)} turnos agendados."
