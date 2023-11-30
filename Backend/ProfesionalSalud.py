from Persistencia import AdministradorDB


class ProfesionalSalud:
    """Esta clase define el estado y el comportamiento de Profesional de Salud"""

    # Constructor
    def __init__(self, id):
        self._id = id

    # Métodos de instancia
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    @classmethod
    def disponibilidad_profesional(self, profesional, fecha, hi, hf):
        admin=AdministradorDB()
        ocupados = admin.consultar_horario_cita_por_profsalud(profesional)
        fecha = fecha.strftime("%Y-%m-%d")
        hi = hi.strftime("%H:%M")
        hf = hf.strftime("%H:%M")
        fechaInicio = fecha + " " + hi
        fechaFin = fecha + " " + hf
        disponible = True
        for fecha in ocupados:
            if fechaInicio == fecha[0] or fechaInicio == fecha[1]:
                disponible = False
                break
            elif fechaInicio > fecha[0] and fechaInicio < fecha[1]:
                disponible = False
                break
            elif fechaFin > fecha[0] and fechaFin < fecha[1]:
                disponible = False
                break
        return disponible