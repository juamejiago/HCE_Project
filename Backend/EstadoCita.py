# Importando el módulo requerido
from enum import Enum


class EstadoCita(Enum):
    CANCELADA = 1
    MODIFICADA = 2
    EJECUTADA = 3
    VERIFICADA = 4
    ANUNCIADA = 5
    AGENDADA = 6
    ACTIVA = 7


