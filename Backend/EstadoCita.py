from enum import Enum
from Persistencia import AdministradorDB


class EstadoCita(Enum):
    CANCELADA = 1
    MODIFICADA = 2
    EJECUTADA = 3
    VERIFICADA = 4
    ANUNCIADA = 5
    AGENDADA = 6
    ACTIVA = 7


