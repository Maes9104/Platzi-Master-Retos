class Autor:
    def __init__(self, id=None, nombre=None, universidad=None, email=None, calificacion_maxima=None, cant_publicaciones=None, promedio_calificacion=None):
        self._id = id
        self._nombre = nombre
        self._universidad = universidad
        self._email = email
        self._calificacion_maxima = calificacion_maxima
        self._cant_publicaciones = cant_publicaciones
        self._promedio_calificacion = promedio_calificacion
    
    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def universidad(self):
        return self._universidad
    
    @universidad.setter
    def set_universidad(self, universidad):
        self._universidad = universidad
    
    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, email):
        self._email = email

    @property
    def calificacion_maxima(self):
        return self._calificacion_maxima

    @calificacion_maxima.setter
    def set_calificacion_maxima(self, calificacion_maxima):
        self._calificacion_maxima = calificacion_maxima

    @property
    def cant_publicaciones(self):
        return self._cant_publicaciones

    @cant_publicaciones.setter
    def set_cant_publicaciones(self, cant_publicaciones):
        self._cant_publicaciones

    @property
    def promedio_calificacion(self):
        return self._promedio_calificacion

    @promedio_calificacion.setter
    def set_promedio_calificacion(self, promedio_calificacion):
        self._promedio_calificacion = promedio_calificacion


    def verificar_calificacion(self):
        pass

    def calcular_promedio(self):
        pass

