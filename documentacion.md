# Instrucciones del Sistema de Gestión Clínica

## Requisitos previos

- Python 3.7 o superior
- No requiere instalar librerías externas (solo la biblioteca estándar de Python)

---

## Cómo ejecutar el sistema

Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

Esto mostrará un menú principal donde puedes elegir:
- Ejecutar el sistema de gestión clínica (opción 1)
- Ejecutar los tests (opción t)
- Salir (opción 0)

---

## Menú del sistema de gestión clínica

Cuando eliges la opción **1) Ejecutar sistema de gestión clínica** desde el menú principal, accederás al menú interno de la clínica.  
Desde allí podrás realizar todas las operaciones principales del sistema.  
Las opciones disponibles son:

- **1) Agregar paciente:** Permite registrar un nuevo paciente en la clínica.
- **2) Agregar médico:** Permite registrar un nuevo médico.
- **3) Agendar turno:** Permite asignar un turno entre un paciente y un médico en una fecha y hora específica.
- **4) Agregar especialidad a médico:** Permite asignar una especialidad y días de atención a un médico existente.
- **5) Emitir receta:** Permite que un médico emita una receta para un paciente.
- **6) Ver historia clínica:** Permite consultar la historia clínica de un paciente, incluyendo turnos y recetas.
- **7) Ver todos los turnos:** Muestra la lista de todos los turnos agendados en la clínica.
- **8) Ver todos los pacientes:** Muestra la lista de pacientes registrados.
- **9) Ver todos los médicos:** Muestra la lista de médicos registrados.
- **0) Salir:** Vuelve al menú principal o cierra el sistema.

Cada opción te guiará paso a paso para ingresar los datos necesarios y te informará si ocurre algún error o si la operación fue exitosa.


## Cómo ejecutar los tests

Tienes dos formas recomendadas:

### 1. Desde el menú principal del sistema

Al iniciar con `python main.py`, elige la opción `t` para ejecutar todos los tests unitarios.  
Verás el resultado directamente en la consola.

### 2. Desde la terminal (modo desarrollador)

Puedes ejecutar todos los tests con:

```bash
python -m unittest discover -s test
```

O ejecutar un test específico, por ejemplo:

```bash
python -m unittest test/test_paciente.py
```

---

## Estructura del proyecto

```
.
├── main.py                # Punto de entrada principal
├── src/
│   ├── CLI.py             # Interfaz de línea de comandos (menú)
│   ├── excepciones.py     # Excepciones personalizadas
│   └── models/
│       ├── clinica.py
│       ├── especialidad.py
│       ├── historia_clinica.py
│       ├── medico.py
│       ├── paciente.py
│       ├── receta.py
│       └── turno.py
└── test/
    ├── test_clinica.py
    ├── test_especialidad.py
    ├── test_historia_clinica.py
    ├── test_medico.py
    ├── test_paciente.py
    ├── test_receta.py
    └── test_turno.py
```

---

## Flujo de uso recomendado

1. Registrar médicos (con sus especialidades y días de atención)
2. Registrar pacientes
3. Agendar turnos entre pacientes y médicos
4. Emitir recetas cuando sea necesario
5. Consultar historias clínicas

---


## Notas

- Todas las validaciones y reglas de negocio están implementadas en las clases del modelo.
- El menú de la CLI captura y muestra los errores de manera amigable.
- Los tests cubren los casos principales y errores esperados.
- Puedes modificar y ampliar el sistema fácilmente siguiendo la estructura actual.

---

profe perdon por tantos commits 