class ProfesionalSalud:
    def __init__(self, especialidad, id, agenda, estado, token):
        self.__token = token
        self.especialidad = especialidad
        self.id = id
        self.agenda = agenda
        self.estado =estado

    # Métodos de clase

    def get_estado(self):
        return self.estado

    def monitorearCita(self):
        pass

    def agendarCita(self):
        pass

    def cancelarCita(self):
        pass

    def modificarCita(self):
        pass

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token