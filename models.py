class Persona:
    def __init__ (self, username, password, direccion, correo, permisos, identificacion):
        self.username=username
        self.password=password
        self.direccion=direccion
        self.correo=correo
        self.permisos=permisos
        self.identificacion=identificacion

class Producto:
    def __init__ (self, precioProducto, idProducto, titleProducto, imagenProducto, categoriaProducto):
        self.precioProducto=precioProducto
        self.idProducto=idProducto
        self.titleProducto=titleProducto
        self.imagenProducto=imagenProducto
        self.categoriaProducto=categoriaProducto
