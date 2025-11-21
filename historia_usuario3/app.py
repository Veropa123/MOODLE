# -*- coding: utf-8 -*-
import servicios as s
import archivos as a

def menu():
    inventario = []

    while True:
        print("\n=== MENÚ ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione una opción (1-9): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    print("Precio y cantidad deben ser números no negativos.")
                    continue
            except ValueError:
                print("Precio o cantidad inválidos.")
                continue

            s.agregar_producto(inventario, nombre, precio, cantidad)
            print(f"Producto '{nombre}' agregado.")

        elif opcion == "2":
            s.mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            prod = s.buscar_producto(inventario, nombre)
            if prod:
                print(f"Encontrado: {prod}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            nuevo_precio = input("Nuevo precio (enter para no cambiar): ")
            nueva_cantidad = input("Nueva cantidad (enter para no cambiar): ")

            np = None
            nc = None
            if nuevo_precio.strip() != "":
                try:
                    np = float(nuevo_precio)
                    if np < 0:
                        print("Precio no puede ser negativo.")
                        continue
                except ValueError:
                    print("Precio inválido.")
                    continue
            if nueva_cantidad.strip() != "":
                try:
                    nc = int(nueva_cantidad)
                    if nc < 0:
                        print("Cantidad no puede ser negativa.")
                        continue
                except ValueError:
                    print("Cantidad inválida.")
                    continue

            actualizado = s.actualizar_producto(inventario, nombre, np, nc)
            if actualizado:
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            eliminado = s.eliminar_producto(inventario, nombre)
            if eliminado:
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            est = s.calcular_estadisticas(inventario)
            if est:
                print("=== Estadísticas del inventario ===")
                print(f"Unidades totales: {est['unidades_totales']}")
                print(f"Valor total: {est['valor_total']}")
                print(f"Producto más caro: {est['producto_mas_caro']['nombre']} - Precio: {est['producto_mas_caro']['precio']}")
                print(f"Producto con mayor stock: {est['producto_mayor_stock']['nombre']} - Cantidad: {est['producto_mayor_stock']['cantidad']}")
            else:
                print("Inventario vacío.")

        elif opcion == "7":
            ruta = "inventario_almacen.csv"
            a.guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = "inventario_almacen.csv"
            cargado, invalidas = a.cargar_csv(ruta)
            if not cargado:
                print("No se cargaron productos.")
                continue
            print(f"Se cargaron {len(cargado)} productos. Filas inválidas: {invalidas}")
            decision = input("¿Sobrescribir inventario? (S/N): ").upper()
            if decision == "S":
                inventario = cargado
                print("Inventario reemplazado.")
            else:
                print("Fusión de inventarios.")
                for p in cargado:
                    existente = s.buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                print("Inventarios fusionados correctamente.")

        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
