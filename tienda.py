class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:  # Si el producto ya existe en la tienda
                prod += producto  # Sumar al stock existente el stock del nuevo ingreso
                break
        else:  # Si el producto no existe en la tienda
            self.__productos.append(producto)

    def listar_productos_farmacia(self):
        lista_productos = ""
        for producto in self.__productos:
            nombre = producto.obtener_nombre
            precio = producto.obtener_precio
            mensaje_envio_gratis = ""  # Inicializamos el mensaje vacío
            if precio >= 15000:
                mensaje_envio_gratis = " (Envío gratis al solicitar este producto)"  # Agregamos el mensaje solo si el precio es mayor o igual a $15000
            lista_productos += f"{nombre}: ${precio}{mensaje_envio_gratis}\n"
        return lista_productos
    def listar_productos_restaurante(self):
        lista_productos = ""
        for producto in self.__productos:
            nombre = producto.obtener_nombre
            precio = producto.obtener_precio
            lista_productos += f"{nombre}: ${precio}\n"
        return lista_productos
    
    def listar_productos_supermercado(self):
        lista_productos = ""
        for producto in self.__productos:
            nombre = producto.obtener_nombre
            precio = producto.obtener_precio
            stock = producto.obtener_stock
            mensaje_pocos_productos = ""  # Inicializamos el mensaje vacío
            if stock < 10:
                mensaje_pocos_productos = " Pocos productos disponibles"  # Agregamos el mensaje solo si el stock es menor a 10
            lista_productos += f"{nombre}: ${precio} - Stock: {stock}{mensaje_pocos_productos}\n"
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        pass
    @property
    def obtener_productos(self):
        return self.__productos
class Restaurante(Tienda):
    pass

class Supermercado(Tienda):
    pass

class Farmacia(Tienda):
    pass
