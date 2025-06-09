from clase_clinica import Clinica
from excepciones import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException
from clase_paciente import Paciente
from clase_medico import Medico
from clase_especialidad import Especialidad
from datetime import datetime

def pedir_fecha_hora():
    while True:
        fecha_str = input("Ingrese fecha y hora (formato: dd/mm/aaaa Hora:Minto): ")
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Formato incorrecto, intente nuevamente.")

def pedir_lista_medicamentos():
    medicamentos = input("Ingrese medicamentos separados por coma:").split(",")
    return [med.strip() for med in medicamentos if med.strip()]

def menu():
    clinica = Clinica()
    while True:
        print("\n Menu de la clinica:")

        print("1) agregar paciente")
        print("2) agregar médico")
        print("3) agendar turno")
        print("4) agregar especialidad a médico")
        print("5) emitir receta")
        print("6) ver historia clínica")
        print("7) ver todos los turnos")
        print("8) ver todos los pacientes")
        print("9) ver todos los médicos")
        print("0) Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1": #agrega pacinete
                nombre = input("nombre del paciente: ")
                dni = input("DNI del paciente: ")
                fecha_nac = input("fecha de nacimiento en formato: dd/mm/aaaa: ")
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("Paciente agregado")


            elif opcion == "2": #agrega medico
                nombre = input("nombre del médico: ")
                matricula = input("matricula profesional: ")
                medico = Medico(nombre, matricula)
                clinica.agregar_medico(medico)
                print("Médico agregado")

            elif opcion == "3": #agrega turno
                dni = input("DNI del paciente: ")
                matricula = input("Matricula del medico: ")
                especialidad = input("Especialidad del medico: ")
                fecha_hora = pedir_fecha_hora()
                clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
                print("Turno agendado")

            elif opcion == "4": #agrega especialidad a medico
                matricula = input("matrícula del médico")
                tipo = input("Especialidad ")
                dias = input("Días de atención por ejemple: lunes, miércoles): ").lower().replace(" ", "").split(",")
                especialidad = Especialidad(tipo, dias)
                medico = clinica.obtener_medico_por_matricula(matricula)

                if medico: #se fija si existe el medico
                    medico.agregar_especialidad(especialidad)
                    print("Especialidad agregada al medico ")
                else:
                    print("medico no se encuentra")

            elif opcion == "5": #emite la receta
                dni = input("DNI del paciente ")
                matricula = input("matricula del médico:")
                medicamentos = pedir_lista_medicamentos()
                clinica.emitir_receta(dni, matricula, medicamentos)
                print("Receta emitida")

            elif opcion == "6": #ve histoCLi
                dni = input("DNI del paciente:")
                historia = clinica.obtener_historia_clinica(dni)
                if historia: #si exite, se muestra, sino el print de abajo
                    print(historia)
                else:
                    print("Historia clínica no se encuentra")

            elif opcion == "7": #ve los turnos
                turnos = clinica.obtener_turnos()
                if turnos:
                    for t in turnos: #again, si esta lo muestra, sino se va al print de abajo
                        print(t)
                else:
                    print("No hay turnos registrados")

            elif opcion == "8": #ve los pacientes
                pacientes = clinica.obtener_pacientes()
                if pacientes:
                    for p in pacientes:
                        print(p)
                else:
                    print("No hay pacientes registrados")

            elif opcion == "9": #ve los medicos
                medicos = clinica.obtener_medicos()
                if medicos:
                    for m in medicos:
                        print(m)
                else:
                    print("No hay médicos registrados.")

            elif opcion == "0": #chau chau
                print("Adios, gracias")
                break

            else:
                print("Opción no valida, Intente de nuevo")

        except (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException, ValueError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()