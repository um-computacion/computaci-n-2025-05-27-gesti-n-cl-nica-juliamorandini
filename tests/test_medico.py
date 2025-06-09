import unittest
from clase_medico import Medico
from clase_especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.nombre = "Dra. Ana Gómez"
        self.matricula = "M1234"
        self.especialidad1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.especialidad2 = Especialidad("Clínica", ["martes"])
        self.medico = Medico(self.nombre, self.matricula, [self.especialidad1])

    def test_constructor(self):
        self.assertEqual(self.medico._Medico__nombre, self.nombre)
        self.assertEqual(self.medico._Medico__matricula, self.matricula)
        self.assertIn(self.especialidad1, self.medico._Medico__especialidades)

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), self.matricula)

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad2)
        self.assertIn(self.especialidad2, self.medico._Medico__especialidades)

    def test_obtener_especialidad_para_dia(self):
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("viernes"))

    def test_str(self):
        resultado = str(self.medico)
        self.assertIn(self.nombre, resultado)
        self.assertIn(self.matricula, resultado)
        self.assertIn("Cardiología", resultado)

if __name__ == "__main__":
    unittest.main()