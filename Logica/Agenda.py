import sqlite3


class Agenda:
    def __init__(self, Bd='HCE_DB.db'):
        self.conexion = sqlite3.connect(Bd)


    def agendaPaciente(self):
        agendaPaciente = 'consultar disponibilidad paciente'

    def agendaProfesionalSalud(self):
        agendaProfesional = 'consultar disponibilidad profesional'

    def agendaInstalacion(self):
        agendaInstalacion = 'consultar disponibilidad instalacion'

    def agendaCita(self):
        agendaCita = 'consultar disponibilidad cita'