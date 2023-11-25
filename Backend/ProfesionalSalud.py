class ProfesionalSalud:
    """Este clase define el estado y el comportamiento de ProfesionalSalud"""

    # Constructor
    def __init__(self, id):
        # Atributos de instancia
        self._id = id

    # Métodos de instancia
    def get__ID(self):
        return self._id
    def set__ID(self, ID):
        self._id = id