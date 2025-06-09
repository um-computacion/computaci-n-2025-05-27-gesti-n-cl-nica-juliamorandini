import unittest
from src.models.clase_medico import Medico
from src.models.clase_especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.esp1 = Especialidad("Cardiología", ["lunes"])
        self.esp2 = Especialidad("Clínica", ["martes"])

    def test_constructor_completo(self):
        m = Medico("Dr. House", "123", [self.esp1])
        self.assertEqual(m.nombre, "Dr. House")
        self.assertEqual(m.matricula, "123")
        self.assertIn(self.esp1, m.especialidades)

    def test_constructor_vacio(self):
        m = Medico()
        self.assertIsNone(m.nombre)
        self.assertIsNone(m.matricula)
        self.assertEqual(m.especialidades, [])

    def test_agregar_especialidad(self):
        m = Medico("Dr. Who", "999", [])
        m.agregar_especialidad(self.esp2)
        self.assertIn(self.esp2, m.especialidades)

    def test_obtener_matricula(self):
        m = Medico("Dr. House", "123", [self.esp1])
        self.assertEqual(m.obtener_matricula(), "123")

    def test_obtener_especialidad_para_dia(self):
        m = Medico("Dr. House", "123", [self.esp1, self.esp2])
        self.assertEqual(m.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(m.obtener_especialidad_para_dia("jueves"))

    def test_str(self):
        m = Medico("Dr. House", "123", [self.esp1])
        s = str(m)
        self.assertIn("Dr. House", s)
        self.assertIn("Matrícula: 123", s)

if __name__ == "__main__":
    unittest.main()