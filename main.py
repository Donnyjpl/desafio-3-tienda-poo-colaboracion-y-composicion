from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

def main():
    # Crear tienda
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado o Farmacia): ")
    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    # Ingresar productos
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre_producto, precio_producto, stock_producto)
        tienda.ingresar_producto(producto)
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break

    # Menú de opciones
    while True:
        print("\nMenú de opciones:")
        print("1. Listar productos existentes")
        print("2. Realizar venta")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            print("\nProductos existentes:")
            print(tienda.listar_productos())
        elif opcion == "2":
            # Implementar lógica para realizar venta
            pass
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")