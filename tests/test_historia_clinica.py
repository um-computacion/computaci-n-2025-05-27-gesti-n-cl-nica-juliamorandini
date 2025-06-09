import unittest
from src.models.clase_historia_clinica import Historia_clinica

class DummyTurno:
    def __str__(self):
        return "Turno Dummy"

class DummyReceta:
    def __str__(self):
        return "Receta Dummy"

class DummyPaciente:
    def __str__(self):
        return "Paciente Dummy"

class TestHistoriaClinica(unittest.TestCase):
    def test_constructor_completo(self):
        p = DummyPaciente()
        turnos = [DummyTurno()]
        recetas = [DummyReceta()]
        h = Historia_clinica(p, turnos, recetas)
        self.assertEqual(h.paciente, p)
        self.assertEqual(h.turnos, turnos)
        self.assertEqual(h.recetas, recetas)

    def test_constructor_vacio(self):
        h = Historia_clinica()
        self.assertIsNone(h.paciente)
        self.assertEqual(h.turnos, [])
        self.assertEqual(h.recetas, [])

    def test_agregar_turnos(self):
        h = Historia_clinica()
        t = DummyTurno()
        h.agregar_turnos(t)
        self.assertIn(t, h.turnos)

    def test_obtener_turnos(self):
        t = DummyTurno()
        h = Historia_clinica(None, [t], [])
        self.assertIn(t, h.turnos)

    def test_obtener_recetas(self):
        r = DummyReceta()
        h = Historia_clinica(None, [], [r])
        self.assertIn(r, h.recetas)

    def test_str(self):
        h = Historia_clinica(DummyPaciente(), [DummyTurno()], [DummyReceta()])
        s = str(h)
        self.assertIn("HistoriaClinica(", s)
        self.assertIn("Turno Dummy", s)
        self.assertIn("Receta Dummy", s)
        self.assertIn("Paciente Dummy", s)

if __name__ == "__main__":
    unittest.main()