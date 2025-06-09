import unittest
from src.models.clase_especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_constructor_completo(self):
        e = Especialidad("Cardiología", ["lunes", "martes"])
        self.assertEqual(e.tipo, "Cardiología")
        self.assertEqual(e.dias, ["lunes", "martes"])

    def test_constructor_vacio(self):
        e = Especialidad()
        self.assertIsNone(e.tipo)
        self.assertEqual(e.dias, [])

    def test_obtener_especialidad(self):
        e = Especialidad("Pediatría", ["viernes"])
        self.assertEqual(e.obtener_especialidad(), "Pediatría")

    def test_verificar_dia(self):
        e = Especialidad("Pediatría", ["viernes"])
        self.assertTrue(e.verificar_dia("Viernes"))
        self.assertFalse(e.verificar_dia("Lunes"))

    def test_str(self):
        e = Especialidad("Pediatría", ["viernes"])
        self.assertIn("Pediatría", str(e))
        self.assertIn("viernes", str(e))

if __name__ == "__main__":
    unittest.main()