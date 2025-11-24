# inventario.py
# Módulo de inventario completamente en español

import csv

inventario = {
    1: {"nombre": "Laptop X100", "marca": "Acer", "categoria": "Laptops", "precio": 700, "stock": 10, "garantia": 12},
    2: {"nombre": "Smart TV 50", "marca": "Samsung", "categoria": "TV", "precio": 400, "stock": 15, "garantia": 24},
    3: {"nombre": "Audífonos Bluetooth", "marca": "Sony", "categoria": "Audio", "precio": 60, "stock": 30, "garantia": 6},
    4: {"nombre": "Mouse Gamer", "marca": "Logitech", "categoria": "Accesorios", "precio": 25, "stock": 50, "garantia": 12},
    5: {"nombre": "Tablet T10", "marca": "Lenovo", "categoria": "Tablets", "precio": 250, "stock": 20, "garantia": 12},
}


def agregar_producto():
    try:
        nuevo_id = max(inventario.keys()) + 1
        nombre = input("Nombre del producto: ")
        marca = input("Marca: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio unitario: "))
        stock = int(input("Cantidad en stock: "))
        garantia = int(input("Garantía (meses): "))

        inventario[nuevo_id] = {
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "garantia": garantia
        }

        print("Producto agregado correctamente.")

    except Exception:
        print("Entrada inválida. El producto no fue agregado.")


def ver_productos():
    print("\n--- INVENTARIO ---")
    for pid, datos in inventario.items():
        print(pid, datos)


def actualizar_producto():
    try:
        palabra = input("Ingrese nombre o palabra clave del producto: ").lower()
        pid_encontrado = None

        for pid, datos in inventario.items():
            if palabra in datos["nombre"].lower():
                pid_encontrado = pid
                break

        if not pid_encontrado:
            print("Producto no encontrado.")
            return

        print(f"Producto seleccionado: {inventario[pid_encontrado]['nombre']}")
        campo = input("Campo a actualizar (nombre/marca/categoria/precio/stock/garantia): ").lower()

        if campo not in inventario[pid_encontrado]:
            print("Campo inválido.")
            return

        if campo in ["precio"]:
            nuevo_valor = float(input("Nuevo valor: "))
        elif campo in ["stock", "garantia"]:
            nuevo_valor = int(input("Nuevo valor: "))
        else:
            nuevo_valor = input("Nuevo valor: ")

        inventario[pid_encontrado][campo] = nuevo_valor

        print("Producto actualizado correctamente.")

    except:
        print("Error al actualizar producto.")


def eliminar_producto():
    try:
        pid = int(input("ID del producto a eliminar: "))
        if pid in inventario:
            del inventario[pid]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")
    except:
        print("ID inválido.")


def guardar_inventario_csv(ruta="inventario.csv"):
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["id", "nombre", "marca", "categoria", "precio", "stock", "garantia"])

            for pid, prod in inventario.items():
                escritor.writerow([
                    pid,
                    prod["nombre"],
                    prod["marca"],
                    prod["categoria"],
                    prod["precio"],
                    prod["stock"],
                    prod["garantia"]
                ])

        print("Inventario guardado correctamente.")

    except Exception as e:
        print("Error al guardar CSV:", e)


def cargar_inventario_csv(ruta="inventario.csv"):
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            inventario.clear()

            for fila in lector:
                pid = int(fila["id"])
                inventario[pid] = {
                    "nombre": fila["nombre"],
                    "marca": fila["marca"],
                    "categoria": fila["categoria"],
                    "precio": float(fila["precio"]),
                    "stock": int(fila["stock"]),
                    "garantia": int(fila["garantia"])
                }

        print("Inventario cargado correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")

    except Exception as e:
        print("Error al cargar CSV:", e)
