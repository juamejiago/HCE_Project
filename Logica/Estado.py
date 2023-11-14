from enum import Enum


class EstadoCita(Enum):
    CANCELADA = 1
    MODIFICADA = 2
    EJECUTADA = 3
    VERIFICADA = 4
    ANUNCIADA = 5
    AGENDADA = 6


class Estado:
    def __init__(self, tipo, autor, descripcion, fecha):
        self.__tipo = tipo
        self.__autor = autor
        self.__descripcion = descripcion
        self.__fecha = fecha

    def get__tipo(self):
        return self.__tipo

    def set__tipo(self, value):
        self.__tipo = value

    def get__autor(self):
        return self.__autor

    def set__autor(self, value):
        self.__autor = value

    def get__descripcion(self):
        return self.__descripcion

    def set__descripcion(self, value):
        self.__descripcion = value

    def get__fecha(self):
        return self.__fecha

    def set__fecha(self, value):
        self.__fecha = value
