class Paciente:
    def __init__(self, id, agenda):
        self.__id = id
        self.__agenda = agenda

    # Métodos de clase

    def get__id(self):
        return self.__id

    def set__id(self, value):
        self.__id = value

    def get__agenda(self):
        return self.__agenda

    def set__agenda(self, value):
        self.__agenda = value