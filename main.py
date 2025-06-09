from src.menu import Menu

def main():
    try:
        Menu.menu()
    except KeyboardInterrupt:
        print("\nSistema terminado por usuario")
    except Exception as e:
        print(f"\nError en el sistema: {e}")

if __name__ == "__main__":
    main()