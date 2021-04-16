class Usuario:
    def __init__ (self, username, password, direccion, correo, identificacion):
        self.username=username
        self.password=password
        self.direccion=direccion
        self.correo=correo
        self.identificacion=identificacion

class Administrador:
    def __init__ (self, username, password, direccion, correo, identificacion, permisos):
        self.username=username
        self.password=password
        self.direccion=direccion
        self.correo=correo
        self.identificacion=identificacion
        self.identificacion=identificacion