# Manejar fechas con la librería datetime
"""from datetime import datetime

# datetime_str = '09/19/18 13:55:26'

# dt = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

dt = datetime(2023, 1, 1, 0, 0)

# getting the timestamp
ts = datetime.timestamp(dt)
print(ts)

date_time = datetime.fromtimestamp(ts)

print(date_time)"""

class Cita:
    """Esta clase define el estado y comportamiento de una Cita"""
    # Constructor
    def __init__(self, ID, tipo, fecha, recursos, estado):
        # Atributos de instancia
        self.__ID = ID
        self.__tipo = tipo
        self.__fecha = fecha
        self.__recursos = recursos
        self.estado = estado

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
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self, fecha):
        self.__fecha = fecha
    def get_recursos(self):
        return self.__recursos
    def set_recursos(self, recursos):
        self.__recursos = recursos
    def get_estado(self):
        return self.estado
    def set_id(self, estado):
        self.estado = estado
