from src.models.clinica import Clinica
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
)
from datetime import datetime

def pedir_fecha_hora():
    while True:
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
        hora = input("Ingrese la hora (HH:MM, 24hs): ")
        try:
            return datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            print("Formato inválido. Intente de nuevo.")

def pedir_lista_medicamentos():
    print("Ingrese los medicamentos separados por coma (ej: Paracetamol, Ibuprofeno):")
    entrada = input("> ")
    medicamentos = [m.strip() for m in entrada.split(",") if m.strip()]
    return medicamentos

def pedir_dias():
    print("Ingrese los días de atención separados por coma (ej: lunes, miércoles):")
    entrada = input("> ")
    dias = [d.strip().lower() for d in entrada.split(",") if d.strip()]
    return dias

def main():
    clinica = Clinica()
    while True:
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad a médico")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                nombre = input("Nombre completo: ").strip()
                dni = input("DNI: ").strip()
                fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("Paciente agregado correctamente.")
            elif opcion == "2":
                nombre = input("Nombre completo: ").strip()
                matricula = input("Matrícula: ").strip()
                medico = Medico(nombre, matricula)
                while True:
                    tipo = input("Especialidad (deje vacío para terminar): ").strip()
                    if not tipo:
                        break
                    dias = pedir_dias()
                    especialidad = Especialidad(tipo, dias)
                    medico.agregar_especialidad(especialidad)
                clinica.agregar_medico(medico)
                print("Médico agregado correctamente.")
            elif opcion == "3":
                dni = input("DNI del paciente: ").strip()
                matricula = input("Matrícula del médico: ").strip()
                especialidad = input("Especialidad: ").strip()
                fecha_hora = pedir_fecha_hora()
                clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
                print("Turno agendado correctamente.")
            elif opcion == "4":
                matricula = input("Matrícula del médico: ").strip()
                tipo = input("Especialidad: ").strip()
                dias = pedir_dias()
                especialidad = Especialidad(tipo, dias)
                medico = clinica.obtener_medico_por_matricula(matricula)
                medico.agregar_especialidad(especialidad)
                print("Especialidad agregada correctamente.")
            elif opcion == "5":
                dni = input("DNI del paciente: ").strip()
                matricula = input("Matrícula del médico: ").strip()
                medicamentos = pedir_lista_medicamentos()
                clinica.emitir_receta(dni, matricula, medicamentos)
                print("Receta emitida correctamente.")
            elif opcion == "6":
                dni = input("DNI del paciente: ").strip()
                historia = clinica.obtener_historia_clinica(dni)
                print(historia)
            elif opcion == "7":
                turnos = clinica.obtener_turnos()
                if not turnos:
                    print("No hay turnos registrados.")
                else:
                    for t in turnos:
                        print(t)
            elif opcion == "8":
                pacientes = clinica.obtener_pacientes()
                if not pacientes:
                    print("No hay pacientes registrados.")
                else:
                    for p in pacientes:
                        print(p)
            elif opcion == "9":
                medicos = clinica.obtener_medicos()
                if not medicos:
                    print("No hay médicos registrados.")
                else:
                    for m in medicos:
                        print(m)
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida.")
        except (ValueError, PacienteNoEncontradoException, MedicoNoDisponibleException,
                TurnoOcupadoException, RecetaInvalidaException) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
