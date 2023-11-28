from enum import Enum
from Persistencia import AdministradorDB


class EstadoCita(Enum):
    CANCELADA = 1
    MODIFICADA = 2
    EJECUTADA = 3
    VERIFICADA = 4
    ANUNCIADA = 5
    AGENDADA = 6

    def __init__(self):
        self.instancia = AdministradorDB()

    def modificar_estado_cita(self, id_cita, modificacion):
        cambio = self.instancia.modificar_estado(id_cita, modificacion)
