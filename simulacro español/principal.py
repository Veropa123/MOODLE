# principal.py
# Sistema de Tienda Electrónica (menú principal)

from inventario import (
    agregar_producto,
    ver_productos,
    actualizar_producto,
    eliminar_producto,
    guardar_inventario_csv,
    cargar_inventario_csv
)

from ventas import (
    registrar_venta,
    ver_ventas,
    guardar_ventas_csv,
    cargar_ventas_csv
)

from reportes import (
    reporte_productos_top,
    reporte_ventas_por_marca,
    reporte_ingresos,
    reporte_desempeno_inventario
)



def mostrar_menu():
    print("\n--- SISTEMA DE TIENDA ELECTRÓNICA ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Ver historial de ventas")
    print("7. Reporte: Top productos")
    print("8. Reporte: Ventas por marca")
    print("9. Reporte: Ingresos")
    print("10. Reporte: Rendimiento del inventario")
    print("11. Guardar inventario CSV")
    print("12. Cargar inventario CSV")
    print("13. Guardar ventas CSV")
    print("14. Cargar ventas CSV")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        try:
            if opcion == "1":
                agregar_producto()

            elif opcion == "2":
                ver_productos()

            elif opcion == "3":
                actualizar_producto()

            elif opcion == "4":
                eliminar_producto()

            elif opcion == "5":
                registrar_venta()

            elif opcion == "6":
                ver_ventas()

            elif opcion == "7":
                top_productos()

            elif opcion == "8":
                ventas_por_marca()

            elif opcion == "9":
                reporte_ingresos()

            elif opcion == "10":
                rendimiento_inventario()

            elif opcion == "11":
                guardar_inventario_csv()

            elif opcion == "12":
                cargar_inventario_csv()

            elif opcion == "13":
                guardar_ventas_csv()

            elif opcion == "14":
                cargar_ventas_csv()

            elif opcion == "0":
                print("Saliendo del sistema... ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

        except Exception as e:
            print("Error inesperado:", e)
            print("Volviendo al menú principal...")


if __name__ == "__main__":
    main()
