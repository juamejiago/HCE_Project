class Paciente:
    """Esta clase define el estado y el comportamiento de Paciente"""

    # Constructor
    def __init__(self, id):
        self._id = id

    # Métodos de instancia
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id