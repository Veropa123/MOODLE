
#guardar_csv
def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV.

    Parámetros:
    inventario: lista de diccionarios con claves 'nombre', 'precio', 'cantidad'
    ruta: ruta del archivo donde se guardará
    incluir_header: si True, escribe la primera línea como encabezado
    """
    import csv

    if not inventario:
        print("El inventario está vacío, no se puede guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])
            
            for producto in inventario:
                escritor.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("No tiene permisos para escribir en esta ubicación.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")


def cargar_csv(ruta="inventario_fruver.csv"):         #cargar_csv
    """Carga un inventario desde un archivo CSV válido.
    
    Retorna una lista de productos con la misma estructura que el inventario.
    Ignora filas inválidas y muestra un contador de errores.
    """
    import csv

    inventario_cargado = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector, None)
            
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido. Se requiere: nombre, precio, cantidad")
                return [], 0

            for fila in lector:
                if len(fila) != 3:
                    errores += 1
                    continue
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue
                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except:
                    errores += 1

        return inventario_cargado, errores

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return [], 0
    except UnicodeDecodeError:
        print("Error de codificación del archivo.")
        return [], 0
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
        return [], 0

