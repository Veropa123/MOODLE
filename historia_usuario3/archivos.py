# -*- coding: cp1252 -*-
def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("No se puede guardar: inventario vac�o.")
        return
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("nombre,precio,cantidad\n")
            for p in inventario:
                f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print("Error: sin permisos para escribir.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def cargar_csv(ruta):
    inventario_cargado = []
    filas_invalidas = 0
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        if not lineas:
            print("Archivo vac�o.")
            return [], 0
        encabezado = lineas[0].strip().lower()
        if encabezado != "nombre,precio,cantidad":
            print("Encabezado inv�lido.")
            return [], 0
        for linea in lineas[1:]:
            partes = linea.strip().split(",")
            if len(partes) != 3:
                filas_invalidas += 1
                continue
            nombre, precio, cantidad = partes
            try:
                precio = float(precio)
                cantidad = int(cantidad)
                if precio < 0 or cantidad < 0:
                    raise ValueError()
                inventario_cargado.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            except ValueError:
                filas_invalidas += 1
        return inventario_cargado, filas_invalidas
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificaci�n.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return [], 0
