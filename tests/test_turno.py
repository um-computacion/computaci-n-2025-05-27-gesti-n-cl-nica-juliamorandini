import unittest
import datetime
from src.models.clase_turno import Turno

class DummyPaciente:
    def __str__(self):
        return "Paciente Dummy"

class DummyMedico:
    def __str__(self):
        return "Medico Dummy"

class TestTurno(unittest.TestCase):
    def test_constructor_completo(self):
        p = DummyPaciente()
        m = DummyMedico()
        fecha = datetime.datetime(2025, 6, 10, 11, 30)
        t = Turno(p, m, fecha, "Cardiología")
        self.assertEqual(t.paciente, p)
        self.assertEqual(t.medico, m)
        self.assertEqual(t.fecha_hora, fecha)
        self.assertEqual(t.especialidad, "Cardiología")

    def test_constructor_vacio(self):
        t = Turno()
        self.assertIsNone(t.paciente)
        self.assertIsNone(t.medico)
        self.assertIsNone(t.fecha_hora)
        self.assertIsNone(t.especialidad)

    def test_str(self):
        p = DummyPaciente()
        m = DummyMedico()
        fecha = datetime.datetime(2025, 6, 10, 11, 30)
        t = Turno(p, m, fecha, "Cardiología")
        s = str(t)
        self.assertIn("Turno:", s)
        self.assertIn("Paciente", s)
        self.assertIn("Médico", s)
        self.assertIn("Cardiología", s)

if __name__ == "__main__":
    unittest.main()