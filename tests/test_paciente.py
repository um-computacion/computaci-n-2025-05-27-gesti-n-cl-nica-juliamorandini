import unittest
from clase_paciente import Paciente

class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.nombre = "Juan Perez"
        self.dni = "12345678"
        self.fecha_nacimiento = "01/01/1990"
        self.paciente = Paciente(self.nombre, self.dni, self.fecha_nacimiento)

    def test_constructor(self):
        self.assertEqual(self.paciente._Paciente__nombre, self.nombre)
        self.assertEqual(self.paciente._Paciente__dni, self.dni)
        self.assertEqual(self.paciente._Paciente__fecha_nacimiento, self.fecha_nacimiento)

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), self.dni)

    def test_str(self):
        esperado = f"{self.nombre}, {self.dni}, {self.fecha_nacimiento}"
        self.assertEqual(str(self.paciente), esperado)

if __name__ == "__main__":
    unittest.main()