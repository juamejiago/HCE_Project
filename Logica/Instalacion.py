class Instalacion:
    """Este clase define el estado y el comportamiento de Instalacion"""

    # Constructor
    def __init__(self, ID, tipo, ubicacion, agenda):
        # Atributos de instancia
        self.__ID = ID
        self. __tipo = tipo
        self.__ubicacion = ubicacion
        self.__agenda = agenda

    # Métodos de clase
    # Métodos de instancia
    def get_id(self):
        return self.__ID
    def set_id(self, ID):
        self.__ID = ID
    def get_tipo(self):
       return self.__tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def get_ubicacion(self):
        return self.__ubicacion
    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion
    def get_ubicacion(self):
        return self.__ubicacion
    def set_agenda(self, agenda):
        self.__agenda = agenda
    def get_agenda(self):
        return self.__agenda



