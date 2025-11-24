## reportes.py
# Módulo de reportes completamente en español

from inventario import inventario
from ventas import historial_ventas

# --- REPORTE 1: PRODUCTOS MÁS VENDIDOS ---
def reporte_productos_top():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    contador = {}

    for venta in historial_ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        contador[producto] = contador.get(producto, 0) + cantidad

    ordenados = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("\n--- PRODUCTOS MÁS VENDIDOS ---")
    for producto, total in ordenados:
        print(f"{producto}: {total} unidades")


# --- REPORTE 2: VENTAS POR MARCA ---
def reporte_ventas_por_marca():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    marcas = {}

    for venta in historial_ventas:
        marca = venta["marca"]
        total = venta["total"]

        marcas[marca] = marcas.get(marca, 0.0) + total

    print("\n--- VENTAS POR MARCA ---")
    for marca, total in marcas.items():
        print(f"{marca}: ${total:.2f}")


# --- REPORTE 3: INGRESOS TOTALES ---
def reporte_ingresos():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    total = sum(venta["total"] for venta in historial_ventas)

    print("\n--- REPORTE DE INGRESOS ---")
    print(f"Ingreso total: ${total:.2f}")


# --- REPORTE 4: DESEMPEÑO DE INVENTARIO ---
def reporte_desempeno_inventario():
    print("\n--- INVENTARIO ---")
    for pid, datos in inventario.items():
        print(f"ID: {pid} | {datos['nombre']} | Stock: {datos['stock']} | Precio: ${datos['precio']}")
