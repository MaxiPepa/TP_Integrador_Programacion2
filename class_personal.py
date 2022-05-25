from class_persona import *

class Personal(Persona):

    def __init__(self, nombre, apellido, telefono, direccion, dni, tarea):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__direccion = str(direccion)
        self.__dni = str(dni)
        self.__telefono = str(telefono)
        self.__tarea = str(tarea)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "PER_" + str(self.__dni[-3:])
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

    # Tarea
    @property
    def tarea(self) -> str:
        return self.__tarea
    
    @tarea.setter
    def set_tarea(self, nuevo) -> None:
        self.__tarea = str(nuevo)