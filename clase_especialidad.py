class Especialidad:
    def __init__(self, tipo: str, dias: list[str]): #contructor
        self.__tipo = tipo
        self.__dias = dias  

    def obtener_especialidad(self) -> str:
        return self.__tipo
    
    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in (d.lower() for d in self.__dias)

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
