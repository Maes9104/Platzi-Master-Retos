from Contribucion import Contribucion

class Ponencia(Contribucion):
    
    def __init__(self):
        super().__init__()

    @property
    def eje_tematico(self):
        return self._eje_tematico

    @eje_tematico.setter
    def set_eje_tematico(self, eje_tematico):
        self._eje_tematico = eje_tematico

    @property
    def fecha_publicacion(self):
        return self._fecha_publicacion

    @fecha_publicacion.setter
    def set_fecha_publicacion(self, fecha_publicacion):
        self._fecha_publicacion = fecha_publicacion
    

    