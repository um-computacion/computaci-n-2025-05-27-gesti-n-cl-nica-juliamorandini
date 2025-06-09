import unittest
import datetime
from src.models.clase_receta import Receta

class DummyPaciente:
    def __str__(self):
        return "Paciente Dummy"

class DummyMedico:
    def __str__(self):
        return "Medico Dummy"

class TestReceta(unittest.TestCase):
    def test_constructor_completo(self):
        p = DummyPaciente()
        m = DummyMedico()
        meds = ["Paracetamol", "Ibuprofeno"]
        fecha = datetime.datetime(2025, 6, 9, 15, 0)
        r = Receta(p, m, meds, fecha)
        self.assertEqual(r.paciente, p)
        self.assertEqual(r.medico, m)
        self.assertEqual(r.medicamentos, meds)
        self.assertEqual(r.fecha, fecha)

    def test_constructor_vacio(self):
        r = Receta()
        self.assertIsNone(r.paciente)
        self.assertIsNone(r.medico)
        self.assertEqual(r.medicamentos, [])
        self.assertIsNone(r.fecha)

    def test_str(self):
        p = DummyPaciente()
        m = DummyMedico()
        meds = ["Paracetamol"]
        fecha = datetime.datetime(2025, 6, 9, 15, 0)
        r = Receta(p, m, meds, fecha)
        s = str(r)
        self.assertIn("Receta(", s)
        self.assertIn("Paciente Dummy", s)
        self.assertIn("Medico Dummy", s)
        self.assertIn("Paracetamol", s)

if __name__ == "__main__":
    unittest.main()