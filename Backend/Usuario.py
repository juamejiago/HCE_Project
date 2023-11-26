# Importando los módulos requeridos
from Persistencia import AdministradorDB


class Usuario:
    """Este clase define el estado y el comportamiento de Usuario"""

    # Constructor
    def __init__(self, nombre_usuario, contrasena):
        # Atributos de instancia
        self.__nombre_usuario = nombre_usuario
        self.__contrasena = contrasena

    # Métodos de clase
    @staticmethod
    def verificar_inicio_sesion(username, password):
        # Creando una conexión con la base de datos
        instancia_verificacion_sesion = AdministradorDB()

        # Realizando la consulta a la base de datos
        respuesta_consulta = instancia_verificacion_sesion.consultar_credenciales_sesion(username, password)

        # Si encuentra un registro en base de datos con dichos datos retorna True, en caso contrario retorna False
        if len(respuesta_consulta) != 0:
            return True
        else:
            return False

    # Métodos de instancia
    def get_nombre_usuario(self):
        return self.__nombre_usuario

    def set_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena
