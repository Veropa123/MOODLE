def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
     
    
    # Creamos el diccionario del producto
    producto = {
        "nombre": nombre.strip(),
        "precio": precio,
        "cantidad": cantidad
    }

    # Lo agregamos a la lista inventario
    inventario.append(producto)

    print(f"Producto '{nombre}' agregado correctamente.")


def mostrar_inventario(inventario):
     """Muestra todos los productos del inventario."""

     if not inventario:  # Si la lista está vacía
        print("El inventario está vacío.")
        return
    
     print("\n=== INVENTARIO ===")
     for producto in inventario:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("------------------------")


def buscar_producto(inventario, nombre):
    """Busca un producto por su nombre y lo retorna o retorna None si no existe."""
    
    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre.strip().lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto."""
    
    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre.strip().lower():

            # Solo actualiza si se recibió un valor
            if nuevo_precio is not None:
                producto["precio"] = nuevo_precio
            
            if nueva_cantidad is not None:
                producto["cantidad"] = nueva_cantidad

            print(f"Producto '{nombre}' actualizado correctamente.")
            return True  # Indica que sí se actualizó
        
    print("Producto no encontrado.")
    return False  # Indica que NO se actualizó


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por su nombre."""

    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre.strip().lower():
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return True
    
    print("Producto no encontrado.")
    return False


def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario y retorna un diccionario con los datos."""

    if not inventario:
        print("El inventario está vacío, no hay estadísticas.")
        return None

    unidades_totales = 0
    valor_total = 0

    # Inicializamos con el primer producto
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += producto["precio"] * producto["cantidad"]

        # Más caro
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        # Mayor stock
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    # Retornamos las estadísticas
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

