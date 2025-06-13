from src.CLI import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSistema interrumpido por el usuario. Saliendo...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
