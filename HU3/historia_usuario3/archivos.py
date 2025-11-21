# -*- coding: utf-8 -*-
# -------------------------
# GUARDAR - AGREGAR AL FINAL
# -------------------------

def guardar_csv_agregar(inventario, ruta="inventario_almacen.csv"):
    """Agrega productos al CSV existente con cada valor en su celda"""
    if not inventario:
        print("Inventario vacío. Nada que guardar.")
        return

    try:
        with open(ruta, "a", encoding="utf-8") as archivo:
            for p in inventario:
                archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print(f"✔ Datos agregados a {ruta}")
    except Exception as e:
        print("Error al guardar:", e)


# ------------------------------
# GUARDAR - SOBRESCRIBIR COMPLETO
# ------------------------------

def guardar_csv_sobrescribir(inventario, ruta="inventario_almacen.csv"):
    """Sobrescribe el CSV con encabezado y cada producto en su celda."""
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("nombre, precio, cantidad\n")
            for p in inventario:
                archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print(f" Archivo actualizado completamente: {ruta}")
    except Exception as e:
        print("Error al sobrescribir:", e)


# ------------------------------
# CARGAR CSV
# ------------------------------

def cargar_csv(ruta="inventario_almacen.csv"):
    """Carga productos desde CSV con tolerancia a espacios y comillas."""
    inventario = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print("CSV vacío.")
            return [], 0

        # Limpiar encabezado de espacios y comillas
        encabezado = [h.strip().replace('"', '') for h in lineas[0].strip().split(",")]

        if encabezado != ["nombre", "precio", "cantidad"]:
            print(f"Encabezado CSV inválido: {encabezado}")
            return [], 0

        for linea in lineas[1:]:
            partes = [p.strip().replace('"', '') for p in linea.strip().split(",")]
            if len(partes) != 3:
                filas_invalidas += 1
                continue
            nombre, precio, cantidad = partes
            try:
                precio = float(precio)
                cantidad = int(cantidad)
                if precio < 0 or cantidad < 0:
                    filas_invalidas += 1
                    continue
                inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            except ValueError:
                filas_invalidas += 1

        return inventario, filas_invalidas

    except FileNotFoundError:
        print("Archivo no encontrado:", ruta)
        return [], 0
    except Exception as e:
        print("Error al cargar CSV:", e)
        return [], 0
