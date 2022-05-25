from class_persona import *

class Docente(Persona):
    
    def __init__(self, nombre, apellido, direccion, dni, telefono, telf_urgencia, materia, titulo = "No tiene"):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__direccion = str(direccion)
        self.__dni = str(dni)
        self.__telefono = str(telefono)
        self.__telf_urgencia = str(telf_urgencia)
        self.__materia = str(materia)
        self.__titulo = str(titulo)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "DOC_" + str(self.__dni[-3:])
        return legajo

    @property
    def legajo(self) -> str:
        legajo = self.__legajo
        return legajo

    # Getters y Setters
    # Nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nuevo) -> None:
        self.__nombre = str(nuevo)

    # Apellido
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def set_apellido(self, nuevo) -> None:
        self.__apellido = str(nuevo)
    
    # Dirección
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # Teléfono
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # Teléfono urgencia
    @property
    def telf_urgencia(self) -> str:
        return self.__telf_urgencia
    
    @telf_urgencia.setter
    def set_telf_urgencia(self, nuevo) -> None:
        self.__telf_urgencia = str(nuevo)

    # Materia
    @property
    def materia(self) -> str:
        return self.__materia
    
    @materia.setter
    def set_materia(self, nuevo) -> None:
        self.__materia = str(nuevo)

    # Título
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def set_titulo(self, nuevo) -> None:
        self.__titulo = str(nuevo)
