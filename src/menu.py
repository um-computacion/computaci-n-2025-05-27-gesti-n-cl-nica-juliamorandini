from src.models.clase_clinica import Clinica
from src.models.excepciones import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException
from src.models.clase_paciente import Paciente
from src.models.clase_medico import Medico
from src.models.clase_especialidad import Especialidad
from datetime import datetime
class Menu:
    def __init__(self, clinica):
        self.clinica = clinica

    def mostrar(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Agregar paciente")
            print("2. Agregar médico")
            print("3. Agendar turno")
            print("4. Ver pacientes")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.ver_pacientes()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def agregar_paciente(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        self.clinica.agregar_paciente(Paciente(nombre, dni, nacimiento))
        print("Paciente agregado.")

    def agregar_medico(self):
        nombre = input("Nombre: ")
        matricula = input("Matrícula: ")
        self.clinica.agregar_medico(Medico(nombre, matricula, []))
        print("Médico agregado.")

    def agendar_turno(self):
        # Lógica para agendar turnos usando self.clinica
        pass

    def ver_pacientes(self):
        for paciente in self.clinica.obtener_pacientes():
            print(paciente)