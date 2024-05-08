class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def obtener_nombre(self):
        return self.__nombre
    
    @property
    def obtener_precio(self):
        return self.__precio
    
    @property
    def obtener_stock(self):
        return self.__stock

    @obtener_stock.setter
    def obtener_stock(self, cantidad):
        if cantidad < 0:
            self.__stock = 0
        else:
            self.__stock += cantidad
            
    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def __add__(self, other):
        if self == other:  # Si los productos son iguales
            self.__stock += other.__stock  # Sumar los stocks
        return self  # Devolver el producto actualizado
