class Contribucion:
    def __init__(self):
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def set_titulo(self, titulo):
        self._titulo = titulo

    @property
    def id_autor(self):
        return self._id_autor

    @id_autor.setter
    def set_id_autor(self, id_autor):
        self._id_autor = id_autor

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def set_calificacion(self, calificacion):
        self._calificacion = calificacion
    
    def actualizar_autor(self):
        pass


