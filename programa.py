from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

# Crear tienda
while True:
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = int(input("Ingrese el tipo de tienda (1: Restaurante, 2: Supermercado, 3: Farmacia): "))

    if tipo_tienda == 1:
        tienda = Restaurante(nombre_tienda, costo_delivery)
        break
    elif tipo_tienda == 2:
        tienda = Supermercado(nombre_tienda, costo_delivery)
        break
    elif tipo_tienda == 3:
        tienda = Farmacia(nombre_tienda, costo_delivery)
        break
    else:
        print("Tipo de tienda no válido. Por favor, ingrese 1, 2 o 3.")

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
        if isinstance(tienda, Restaurante):
            print(tienda.listar_productos_restaurante())
        elif isinstance(tienda, Farmacia):
            print(tienda.listar_productos_farmacia())
        else:
            print(tienda.listar_productos_supermercado())
    

    elif opcion == "2":
        # Realizar venta
        nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
        cantidad = int(input("Ingrese la cantidad requerida: "))

        if isinstance(tienda, Restaurante):
            print("Los productos del restaurante siempre tienen stock 0.")
        elif isinstance(tienda, Farmacia):
            if cantidad > 3:
                print("No se puede solicitar una cantidad superior a 3 por producto en cada venta.")
            else:
                for producto in tienda.obtener_productos():
                    if producto.obtener_nombre() == nombre_producto:
                        stock_disponible = producto.obtener_stock()
                        cantidad_vendida = min(cantidad, stock_disponible)
                        producto.modificar_stock(-cantidad_vendida)
                        print(f"Se vendieron {cantidad_vendida} unidades de {nombre_producto}.")
                        break
                else:
                    print("El producto solicitado no existe en la tienda")
        elif isinstance(tienda, Supermercado):
            for producto in tienda.obtener_productos():    
                if producto.obtener_nombre() == nombre_producto:
                    stock_disponible = producto.obtener_stock()
                    if cantidad <= stock_disponible:
                        producto.modificar_stock(-cantidad)
                        print(f"Se vendieron {cantidad} unidades de {nombre_producto}.")
                    else:
                        producto.modificar_stock(-stock_disponible)
                        print(f"Se vendieron {stock_disponible} unidades de {nombre_producto}.")
                    break
            else:
                print("El producto solicitado no existe en la tienda")

    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
