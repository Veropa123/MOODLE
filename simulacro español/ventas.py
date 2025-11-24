# ventas.py
# Módulo de ventas completamente en español

import csv
from inventario import inventario

historial_ventas = []

# Descuentos por tipo de cliente
descuentos = {
    "regular": 0.00,
    "premium": 0.10,
    "vip": 0.20
}


def registrar_venta():
    try:
        cliente = input("Nombre del cliente: ")
        tipo_cliente = input("Tipo de cliente (regular/premium/vip): ").lower()
        palabra = input("Nombre o palabra clave del producto: ").lower()
        cantidad = int(input("Cantidad: "))

        # Buscar producto por nombre
        id_encontrado = None
        for pid, datos in inventario.items():
            if palabra in datos["nombre"].lower():
                id_encontrado = pid
                break

        if not id_encontrado:
            print("Producto no encontrado.")
            return

        producto = inventario[id_encontrado]

        # Validar stock
        if producto["stock"] < cantidad:
            print("Stock insuficiente.")
            return

        # Aplicar descuento (LAMBDA requerida por el simulacro)
        descuento = descuentos.get(tipo_cliente, 0)
        calcular_total = lambda precio, cantidad: precio * cantidad * (1 - descuento)

        total = calcular_total(producto["precio"], cantidad)

        # Actualizar inventario
        producto["stock"] -= cantidad

        # Guardar venta
        venta = {
            "cliente": cliente,
            "tipo_cliente": tipo_cliente,
            "producto": producto["nombre"],
            "marca": producto["marca"],
            "cantidad": cantidad,
            "descuento": descuento,
            "total": total
        }

        historial_ventas.append(venta)
        print("Venta registrada correctamente.")

    except Exception:
        print("Error al registrar la venta.")


def ver_ventas():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- HISTORIAL DE VENTAS ---")
    for v in historial_ventas:
        print(v)


def guardar_ventas_csv(ruta="ventas.csv"):
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["cliente", "tipo_cliente", "producto", "marca", "cantidad", "descuento", "total"])

            for venta in historial_ventas:
                escritor.writerow([
                    venta["cliente"],
                    venta["tipo_cliente"],
                    venta["producto"],
                    venta["marca"],
                    venta["cantidad"],
                    venta["descuento"],
                    venta["total"]
                ])

        print("Ventas guardadas correctamente.")

    except Exception as e:
        print("Error al guardar CSV:", e)
        
def cargar_ventas_csv(ruta="ventas.csv"):
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            historial_ventas.clear()

            for fila in lector:
                historial_ventas.append({
                    "cliente": fila["cliente"],
                    "tipo_cliente": fila["tipo_cliente"],
                    "producto": fila["producto"],
                    "marca": fila["marca"],
                    "cantidad": int(fila["cantidad"]),
                    "descuento": float(fila["descuento"]),
                    "total": float(fila["total"])
                })

        print("Ventas cargadas correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo ventas.csv.")

    except Exception as e:
        print("Error al cargar ventas CSV:", e)