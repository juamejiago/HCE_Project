class Cita:
    """Esta clase define el estado y comportamiento de una Cita"""

    # Constructor
    def __init__(self, id, id_paciente_asociado, id_instalacion_asociada, id_profesionalSalud_asociado, tipo, estado,
                 fecha_inicio, fecha_finalizacion):
        # Atributos de instancia
        self._id = id
        self._id_paciente_asociado = id_paciente_asociado
        self._id_instalacion_asociada = id_instalacion_asociada
        self._id_profesionalSalud_asociado = id_profesionalSalud_asociado
        self._tipo = tipo
        self._estado = estado
        self._fecha_inicio = fecha_inicio
        self._fecha_finalizacion = fecha_finalizacion

    # Métodos de instancia
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_id_paciente_asociado(self):
        return self._id_paciente_asociado

    def set_id_paciente_asociado(self, id_paciente_asociado):
        self._id_paciente_asociado = id_paciente_asociado

    def get_id_instalacion_asociada(self):
        return self._id_instalacion_asociada

    def set_id_instalacion_asociada(self, id_instalacion_asociada):
        self._id_instalacion_asociada = id_instalacion_asociada

    def get_id_profesionalSalud_asociado(self):
        return self._id_profesionalSalud_asociado

    def set_id_profesionalSalud_asociado(self, id_profesionalSalud_asociado):
        self._id_profesionalSalud_asociado = id_profesionalSalud_asociado

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def get_fecha_finalizacion(self):
        return self._fecha_finalizacion

    def set_fecha_finalizacion(self, fecha_finalizacion):
        self._fecha_finalizacion = fecha_finalizacion