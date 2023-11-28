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

        # NO PONER ACÁ PORFA
        # self.instancia = AdministradorDB()

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

    def modificar_paciente(self, pacienteNuevo, id_cita):
        '''Consultar si el paciente ya tiene una cita asignada, si esa hora se traspala con esta modificacion
        buscar otra fecha.'''
        consultarPacienteNuevo = self.instancia.consultar_pacientes()
        if consultarPacienteNuevo:
            cambio = self.instancia.modifciar_paciente_cita(id_cita, pacienteNuevo)

    def modificar_instalacion(self, id):
        '''La idea es consultar si la instalacion a modificar ya está asignada por medio de la clave foranea
        a una cita, para después consultar si para la fehca que se desea usar esa instalacion ya esta siendo
        utilizada por la cita asignada. Si no lo está, se modifica la cita, si lo está, se busca otra fecha.'''
        pass

    def modificar_tipo_cita(self):
        pass

    def modificar_fecha(self):
        pass

    def monitorear_cita(self):
        pass
