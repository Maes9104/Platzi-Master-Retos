from Contribucion import Contribucion

class Taller:
    def __init__(self):
        super().__init__()

    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima

    @capacidad_maxima.setter
    def set_capacidad_maxima(self, capacidad_maxima):
        self._capacidad_maxima = capacidad_maxima

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def set_duracion(self, duracion):
        self._duracion = duracion