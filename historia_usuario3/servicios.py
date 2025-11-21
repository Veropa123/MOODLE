# -*- coding: utf-8 -*-


def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' agregado correctamente.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n=== INVENTARIO ===")
    for p in inventario:
        print(f"- {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print("==================\n")

def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print("Producto no encontrado.")
        return False
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    print(f"Producto '{nombre}' actualizado correctamente.")
    return True

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"Producto '{nombre}' eliminado.")
        return True
    print("Producto no encontrado.")
    return False

def calcular_estadisticas(inventario):
    if not inventario:
        print("No hay productos para mostrar estadísticas.")
        return None
    subtotal = lambda p: p["precio"] * p["cantidad"]
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
