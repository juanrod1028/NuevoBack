class Persona:
    def __init__ (self, username, password, direccion, correo, permisos, identificacion):
        self.username=username
        self.password=password
        self.direccion=direccion
        self.correo=correo
        self.permisos=permisos
        self.identificacion=identificacion

class Producto:
    def __init__ (self, idProducto, nombreProducto, precioProducto, imagenProducto, estadoProducto):
        self.idProducto=idProducto
        self.Producto=nombreProducto
        self.precioProducto=precioProducto
        self.imagenProducto=imagenProducto
        self.estadoProducto=estadoProducto
