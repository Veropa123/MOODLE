# -*- coding: utf-8 -*-
import servicios as s
import archivos as a

# Definición del archivo de inventario
NOMBRE_ARCHIVO_CSV = "inventario_almacen.csv"

def menu(inventario):
    """
    Función principal que maneja el menú y la interacción con el usuario.
    Recibe el inventario cargado inicialmente.
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar y Salir (Sobrescribir CSV)")
        print("8. Recargar/Fusionar CSV")
        print("9. Salir sin Guardar")

        opcion = input("Seleccione una opción (1-9): ")

        # --------------------------- OPCIÓN 1: Agregar producto ---------------------------
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    print("⛔ Error: Precio y cantidad deben ser números no negativos.")
                    continue
            except ValueError:
                print("⛔ Error: Precio o cantidad inválidos.")
                continue

            # La función maneja si debe agregar uno nuevo o actualizar uno existente (evita duplicados)
            s.agregar_producto(inventario, nombre, precio, cantidad)
            print(f"✔ Producto '{nombre}' agregado/actualizado correctamente.")

        # --------------------------- OPCIÓN 2: Mostrar inventario ---------------------------
        elif opcion == "2":
            s.mostrar_inventario(inventario)

        # --------------------------- OPCIÓN 3: Buscar producto ---------------------------
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            prod = s.buscar_producto(inventario, nombre)
            if prod:
                print(f"Producto encontrado: {prod}")
            else:
                print("Producto no encontrado.")

        # --------------------------- OPCIÓN 4: Actualizar producto ---------------------------
        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")

            nuevo_precio = input("Nuevo precio (ENTER para no cambiar): ")
            nueva_cantidad = input("Nueva cantidad (ENTER para no cambiar): ")

            np = None
            nc = None

            if nuevo_precio.strip() != "":
                try:
                    np = float(nuevo_precio)
                except ValueError:
                    print("⛔ Error: Precio inválido.")
                    continue

            if nueva_cantidad.strip() != "":
                try:
                    nc = int(nueva_cantidad)
                except ValueError:
                    print("⛔ Error: Cantidad inválida.")
                    continue

            actualizado = s.actualizar_producto(inventario, nombre, np, nc)
            if actualizado:
                print("✔ Producto actualizado.")
            else:
                print("Producto no encontrado.")

        # --------------------------- OPCIÓN 5: Eliminar producto ---------------------------
        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            eliminado = s.eliminar_producto(inventario, nombre)
            if eliminado:
                print("✔ Producto eliminado.")
            else:
                print("Producto no encontrado.")

        # --------------------------- OPCIÓN 6: Estadísticas ---------------------------
        elif opcion == "6":
            est = s.calcular_estadisticas(inventario)
            if est:
                print("\n=== ESTADÍSTICAS ===")
                print(f"Número total de productos distintos: {len(inventario)}")
                print(f"Unidades totales en stock: {est['unidades_totales']}")
                print(f"Valor total del inventario: ${est['valor_total']:.2f}")
                print(f"Producto más caro: {est['producto_mas_caro']['nombre']} (${est['producto_mas_caro']['precio']:.2f})")
                print(f"Producto con mayor stock: {est['producto_mayor_stock']['nombre']} ({est['producto_mayor_stock']['cantidad']} unidades)")
            else:
                print("El inventario está vacío.")

        # --------------------------- OPCIÓN 7: Guardar y Salir ---------------------------
        elif opcion == "7":
            # Usa sobrescribir ('w') para guardar el estado actual de la memoria (limpio de duplicados)
            print(f"\nGuardando inventario en '{NOMBRE_ARCHIVO_CSV}' y saliendo...")
            try:
                a.guardar_csv_sobrescribir(inventario, NOMBRE_ARCHIVO_CSV)
                print("✔ Inventario guardado correctamente.")
            except Exception as e:
                print(f"⛔ Error al guardar el CSV: {e}")
            break

        # --------------------------- OPCIÓN 8: Recargar/Fusionar CSV ---------------------------
        elif opcion == "8":
            archivo_carga = input(f"Ingrese el nombre del archivo CSV a cargar (o deje vacío para '{NOMBRE_ARCHIVO_CSV}'): ").strip()
            if not archivo_carga:
                archivo_carga = NOMBRE_ARCHIVO_CSV

            print(f"\nCargando productos desde '{archivo_carga}'...")
            
            cargado, invalidas = a.cargar_csv(archivo_carga)

            if not cargado:
                print("⚠ No se cargaron productos válidos del archivo.")
                if invalidas > 0:
                     print(f"Se encontraron {invalidas} filas con formato incorrecto o faltante.")
                continue

            print(f"✔ Se cargaron {len(cargado)} productos del archivo. Filas inválidas: {invalidas}")

            # Lógica de sobrescribir o fusionar
            decision = input("¿Desea (R)eemplazar el inventario actual o (F)usionar los datos? (R/F): ").upper()

            if decision == "R":
                inventario.clear()
                inventario.extend(cargado)
                print("Inventario reemplazado completamente.")
            elif decision == "F":
                print("Fusionando inventarios...")
                # Llama a la función fusionar_inventarios
                productos_fusionados = s.fusionar_inventarios(inventario, cargado)
                inventario.clear()
                inventario.extend(productos_fusionados)
                print("Inventarios fusionados correctamente.")
            else:
                print("Opción inválida. Los datos cargados no se aplicaron.")

        # --------------------------- OPCIÓN 9: Salir sin Guardar --------------------
        elif opcion == "9":
            print("Saliendo sin guardar cambios...")
            break

        # --------------------------- OPCIÓN INVÁLIDA --------------------
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    inventario_actual = []
    
    # Intenta cargar el inventario al inicio del programa
    print(f"Iniciando: Intentando cargar inventario desde '{NOMBRE_ARCHIVO_CSV}'...")
    
    try:
        inventario_cargado, errores = a.cargar_csv(NOMBRE_ARCHIVO_CSV)
        
        if inventario_cargado:
            inventario_actual.extend(inventario_cargado)
            print(f"✔ Inventario inicial cargado con {len(inventario_cargado)} productos.")
        else:
            print("⚠ Archivo CSV no encontrado o vacío. Comenzando con inventario vacío.")
        
        if errores > 0:
            print(f"⚠ Se omitieron {errores} filas inválidas durante la carga inicial.")
            
    except Exception as e:
        print(f"⛔ Error en la carga inicial: {e}. Comenzando con inventario vacío.")
        
    menu(inventario_actual)