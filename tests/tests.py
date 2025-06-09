import unittest
from clase_clinica import Clinica
from excepciones import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException
from clase_paciente import Paciente
from clase_medico import Medico
from clase_especialidad import Especialidad
from datetime import datetime

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.otro_paciente = Paciente("Ana Gomez", "87654321", "05/05/1985")
        self.medico = Medico("Dra. Lopez", "M123", [])
        self.otro_medico = Medico("Dr. House", "H001", [])
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.otra_especialidad = Especialidad("Cardiología", ["martes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.otro_medico.agregar_especialidad(self.otra_especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_paciente(self.otro_paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.agregar_medico(self.otro_medico)   

    def test_agregar_paciente_existente(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico_existente(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)

    def test_obtener_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        self.assertIn(self.paciente, pacientes)
        self.assertIn(self.otro_paciente, pacientes)

    def test_obtener_medicos(self):
        medicos = self.clinica.obtener_medicos()
        self.assertIn(self.medico, medicos)
        self.assertIn(self.otro_medico, medicos)

    def test_agendar_turno_ok(self):
        fecha = datetime.strptime("09/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "M123", "Pediatría", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M123")
        self.assertEqual(turnos[0].obtener_paciente().obtener_dni(), "12345678")

    def test_agendar_turno_paciente_no_existe(self):
        fecha = datetime.strptime("09/06/2025 10:00", "%d/%m/%Y %H:%M")
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M123", "Pediatría", fecha)

    def test_agendar_turno_medico_no_existe(self):
        fecha = datetime.strptime("09/06/2025 10:00", "%d/%m/%Y %H:%M")
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M999", "Pediatría", fecha)

    def test_agendar_turno_especialidad_incorrecta(self):
        fecha = datetime.strptime("10/06/2025 10:00", "%d/%m/%Y %H:%M")  # martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M123", "Cardiología", fecha)

    def test_agendar_turno_dia_no_disponible(self):
        fecha = datetime.strptime("11/06/2025 10:00", "%d/%m/%Y %H:%M")  # miércoles, pero especialidad es martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "H001", "Cardiología", fecha)

    def test_agendar_turno_duplicado(self):
        fecha = datetime.strptime("09/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "M123", "Pediatría", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M123", "Pediatría", fecha)

    def test_emitir_receta_ok(self):
        fecha = datetime.strptime("09/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "M123", "Pediatría", fecha)
        self.clinica.emitir_receta("12345678", "M123", ["Paracetamol", "Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertTrue(any("Paracetamol" in str(r) for r in historia.recetas))

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "M123", ["Paracetamol"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("12345678", "M999", ["Paracetamol"])

    def test_emitir_receta_vacia(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M123", [])

    def test_historia_clinica_vacia(self):
        historia = self.clinica.obtener_historia_clinica("87654321")
        self.assertIsNotNone(historia)
        self.assertEqual(len(historia.recetas), 0)

    def test_agregar_especialidad_repetida(self):
        otra = Especialidad("Pediatría", ["viernes"])
        self.medico.agregar_especialidad(otra)
        especialidades = self.medico.obtener_especialidades()
        self.assertEqual(len([e for e in especialidades if e.tipo == "Pediatría"]), 1)

    def test_str_paciente(self):
        self.assertIsInstance(str(self.paciente), str)
        self.assertIn("Juan Perez", str(self.paciente))

if __name__ == '__main__':
    unittest.main()