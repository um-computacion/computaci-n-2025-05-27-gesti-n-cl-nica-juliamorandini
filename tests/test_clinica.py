import unittest
from src.models.clase_clinica import Clinica, PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException
from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
from src.models.clase_turno import Turno
from src.models.clase_historia_clinica import Historia_clinica

import datetime

class DummyHistoriaClinica:
    def __init__(self, paciente, turnos=None, recetas=None):
        self.turnos = turnos or []
        self.recetas = recetas or []
        self.paciente = paciente
    def agregar_turno(self, turno):
        self.turnos.append(turno)

class DummyTurno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.especialidad = especialidad

class DummyMedico(Medico):
    def __init__(self, nombre="Dr. X", matricula="111", especialidades=None):
        super().__init__(nombre, matricula, especialidades or [])
    def obtener_matricula(self):
        return self._Medico__matricula

class DummyPaciente(Paciente):
    def __init__(self, nombre="Paciente X", dni="222", fecha="01/01/2000"):
        super().__init__(nombre, dni, fecha)
    def obtener_dni(self):
        return self._Paciente__dni

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = DummyPaciente("Juan", "123", "01/01/2000")
        self.medico = DummyMedico("Ana", "456", [])
        self.historia = DummyHistoriaClinica(self.paciente)
        self.clinica = Clinica(
            pacientes={"123": self.paciente},
            medicos={"456": self.medico},
            turnos=[],
            historias_clinica={"123": self.historia}
        )

    def test_agregar_paciente_y_duplicado(self):
        nuevo = DummyPaciente("Pepe", "999", "01/01/2001")
        self.clinica.agregar_paciente(nuevo)
        self.assertIn("999", self.clinica._Clinica__pacientes)
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(nuevo)

    def test_agregar_medico_y_duplicado(self):
        nuevo = DummyMedico("Dr. Z", "888")
        self.clinica.agregar_medico(nuevo)
        self.assertIn("888", self.clinica._Clinica__medicos)
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(nuevo)

    def test_obtener_pacientes_y_medicos(self):
        pacientes = self.clinica.obtener_pacientes()
        medicos = self.clinica.obtener_medicos()
        self.assertIn(self.paciente, pacientes)
        self.assertIn(self.medico, medicos)

    def test_obtener_medico_por_matricula(self):
        self.assertEqual(self.clinica.obtener_medico_por_matricula("456"), self.medico)

    def test_obtener_turnos(self):
        self.assertIsInstance(self.clinica.obtener_turnos(), list)

    def test_obtener_historia_clinica(self):
        self.assertEqual(self.clinica.obtener_historia_clinica("123"), self.historia)

    def test_agendar_turno_excepciones(self):
        # Paciente no existe
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("noexiste", "456", "Cardiología", datetime.datetime.now())
        # Medico no existe
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("123", "noexiste", "Cardiología", datetime.datetime.now())

    # Puedes seguir agregando tests para validar duplicidad de turnos, especialidad/día, etc.

if __name__ == "__main__":
    unittest.main()