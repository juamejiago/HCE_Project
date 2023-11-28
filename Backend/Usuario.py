# Importando los módulos requeridos
from Persistencia import AdministradorDB


class Usuario:
    """Esta clase define el estado y el comportamiento de Usuario"""

    # Constructor
    def __init__(self, id, contrasena):
        # Atributos de instancia
        self._id = id
        self._contrasena = contrasena

    # Métodos de clase
    @staticmethod
    def verificar_inicio_sesion(password, id):
        # Creando una conexión con la base de datos
        instancia_verificacion_sesion = AdministradorDB()

        # Realizando la consulta a la base de datos
        respuesta_consulta = instancia_verificacion_sesion.consultar_credenciales_sesion(password, id)

        # Cerrando conexión con la base de datos
        instancia_verificacion_sesion.cerrar_conexion_db()

        # Si encuentra un registro en base de datos con dichos datos retorna True, en caso contrario retorna False
        if len(respuesta_consulta) != 0:
            return True
        else:
            return False

    # Métodos de instancia
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_contrasena(self):
        return self._contrasena

    def set_contrasena(self, contrasena):
        self._contrasena = contrasena
