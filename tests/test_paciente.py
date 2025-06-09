import unittest
from src.models.clase_paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_constructor_completo(self):
        p = Paciente("Juan", "123", "01/01/2000")
        self.assertEqual(p.nombre, "Juan")
        self.assertEqual(p.dni, "123")
        self.assertEqual(p.fecha_nacimiento, "01/01/2000")

    def test_constructor_vacio(self):
        p = Paciente()
        self.assertIsNone(p.nombre)
        self.assertIsNone(p.dni)
        self.assertIsNone(p.fecha_nacimiento)

    def test_obtener_dni(self):
        p = Paciente("Ana", "456", "02/02/2002")
        self.assertEqual(p.obtener_dni(), "456")

    def test_str(self):
        p = Paciente("Ana", "456", "02/02/2002")
        self.assertEqual(str(p), "Ana, 456, 02/02/2002")

if __name__ == "__main__":
    unittest.main()