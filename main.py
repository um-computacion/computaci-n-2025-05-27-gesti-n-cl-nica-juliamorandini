from src.CLI import main
import sys
import unittest

def run_tests():
    print("\nEjecutando tests...\n")
    loader = unittest.TestLoader()
    tests = loader.discover('test')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)
    if result.wasSuccessful():
        print("\nTodos los tests pasaron correctamente.\n")
    else:
        print(f"\nAlgunos tests fallaron. Fallos: {len(result.failures)}, Errores: {len(result.errors)}\n")

if __name__ == "__main__":
    try:
        while True:
            print("\nSeleccione una opción:")
            print("1) Ejecutar sistema de gestión clínica")
            print("t) Ejecutar tests")
            print("0) Salir")
            opcion = input("> ").strip().lower()
            if opcion == "1":
                main()
            elif opcion == "t":
                run_tests()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida.")
    except KeyboardInterrupt:
        print("\nSistema interrumpido por el usuario. Saliendo...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
