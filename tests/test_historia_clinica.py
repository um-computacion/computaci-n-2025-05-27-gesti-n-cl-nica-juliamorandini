import unittest
from clase_historia_clinica import Historia_clinica
from clase_paciente import Paciente
from clase_turno import Turno
from clase_receta import Receta

class DummyTurno:
    def __str__(self):
        return "Turno de prueba"

class DummyReceta:
    def __str__(self):
        return "Receta de prueba"

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Carlos Lopez", "98765432", "10/10/1982")
        self.turno1 = DummyTurno()
        self.turno2 = DummyTurno()
        self.receta1 = DummyReceta()
        self.receta2 = DummyReceta()
        self.historia = Historia_clinica(self.paciente, [self.turno1], [self.receta1])

    def test_constructor(self):
        self.assertEqual(self.historia._Historia_clinica__paciente, self.paciente)
        self.assertIn(self.turno1, self.historia._Historia_clinica__turnos)
        self.assertIn(self.receta1, self.historia._Historia_clinica__recetas)

    def test_agregar_turnos(self):
        self.historia.agregar_turnos(self.turno2)
        self.assertIn(self.turno2, self.historia.obtener_turnos())

    def test_obtener_turnos(self):
        turnos = self.historia.obtener_turnos()
        self.assertIn(self.turno1, turnos)
        self.assertTrue(isinstance(turnos, list))

    def test_obtener_recetas(self):
        recetas = self.historia.obtener_recetas()
        self.assertIn(self.receta1, recetas)
        self.assertTrue(isinstance(recetas, list))

    def test_str(self):
        output = str(self.historia)
        self.assertIn("HistoriaClinica(", output)
        self.assertIn("Turno de prueba", output)
        self.assertIn("Receta de prueba", output)
        self.assertIn(str(self.paciente), output)

if __name__ == "__main__":
    unittest.main()