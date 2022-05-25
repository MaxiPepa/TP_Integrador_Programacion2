from os import get_terminal_size
from class_persona import *

class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cant_hermanos, telf_madre, telf_padre, telf_adicional) -> None:
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__dni = str(dni)
        self.__direccion = str(direccion)
        self.__telefono = str(telefono)
        self.__email = str(email)
        self.__nacionalidad = str(nacionalidad)
        self.__residencia = str(residencia)
        self.__cant_hermanos = str(cant_hermanos)
        self.__telf_madre = str(telf_madre)
        self.__telf_padre = str(telf_padre)
        self.__telf_adicional = str(telf_adicional)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "ALU_" + str(self.__dni[-3:])
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
    
    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # Dirección
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # Teléfono
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # Email
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def set_email(self, nuevo) -> None:
        self.__email = str(nuevo)
    
    # Nacionalidad
    @property
    def nacionalidad(self) -> str:
        return self.__nacionalidad
    
    @nacionalidad.setter
    def set_nacionalidad(self, nuevo) -> None:
        self.__nacionalidad = str(nuevo)

    # Residencia
    @property
    def residencia(self) -> str:
        return self.__residencia
    
    @residencia.setter
    def set_residencia(self, nuevo) -> None:
        self.__residencia = str(nuevo)

    # Cantidad Hemanos
    @property
    def cant_hermanos(self) -> str:
        return self.__cant_hermanos
    
    @cant_hermanos.setter
    def set_cant_hermanos(self, nuevo) -> None:
        self.__cant_hermanos = str(nuevo)

    # Teléfono madre
    @property
    def telf_madre(self) -> str:
        return self.__telf_madre
    
    @telf_madre.setter
    def set_telf_madre(self, nuevo) -> None:
        self.__telf_madre = str(nuevo)

    # Teléfono padre
    @property
    def telf_padre(self) -> str:
        return self.__telf_padre
    
    @telf_padre.setter
    def set_telf_padre(self, nuevo) -> None:
        self.__telf_padre = str(nuevo)

    # Teléfono adicional
    @property
    def telf_adicional(self) -> str:
        return self.__telf_adicional
    
    @telf_adicional.setter
    def set_telf_adicional(self, nuevo) -> None:
        self.__telf_adicional = str(nuevo)