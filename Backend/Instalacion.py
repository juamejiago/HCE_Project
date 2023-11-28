class Instalacion:
    """Esta clase define el estado y el comportamiento de Instalacion"""

    # Constructor
    def __init__(self, id):
        self._id = id

    # Métodos de instancia
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id