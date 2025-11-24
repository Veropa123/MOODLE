from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas 
from archivos import guardar_csv, cargar_csv


def main():
    inventario = []

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": # Agregar producto
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio: "))
            cantidad = int(input("Ingrese cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)
        
        elif opcion == "2": # Mostrar inventario
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
             
            producto = buscar_producto(inventario, nombre)
            if producto:
                print("Producto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
            else:
                print("Producto no encontrado.")



        elif opcion == "4":  # Actualizar producto
            nombre = input("Ingrese el nombre del producto a actualizar: ")

             # Buscar si existe
            producto = buscar_producto(inventario, nombre)
            if not producto:
                print("Producto no encontrado.")
                continue

            print("Deje el campo vacío si NO desea modificarlo.")
    
             # Solicitar nuevos valores
            nuevo_precio_str = input("Nuevo precio: ")
            nueva_cantidad_str = input("Nueva cantidad: ")

             # Convertir solo si no está vacío
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str.strip() != "" else None
            nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str.strip() != "" else None

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
        
        
        elif opcion == "5":  # Eliminar producto
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)
            
        elif opcion == "6":  # Estadísticas
            stats = calcular_estadisticas(inventario)
    
            if stats:  # Si hay datos
                print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: {stats['valor_total']}")
                print(f"Producto más caro: {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']})")
                print(f"Producto con mayor stock: {stats['producto_mayor_stock']['nombre']} ({stats['producto_mayor_stock']['cantidad']} unidades)")

        elif opcion == "7":  # Guardar CSV
            ruta = input("Ingrese la ruta o nombre del archivo CSV a guardar: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":  # Cargar CSV
           ruta = input("Ingrese la ruta o nombre del archivo CSV a cargar: ")
        # Inicializamos variables por seguridad
           inventario_cargado = []
           errores = 0

        # Intentamos cargar el CSV
        try:
            inventario_cargado, errores = cargar_csv(ruta)
        except Exception as e:
            print(f"Ocurrió un error al cargar el archivo: {e}")
            # No usamos ruta dentro del except, solo mostramos el error
            inventario_cargado = []
            errores = 0

            if not inventario_cargado:
                print(f"No se cargó ningún producto. Filas inválidas omitidas: {errores}")
                continue

    # Preguntar al usuario si quiere sobrescribir
            respuesta = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if respuesta == "S":
                inventario = inventario_cargado
                print(f"Inventario reemplazado. Productos cargados: {len(inventario_cargado)}. Filas inválidas omitidas: {errores}")
            else:
        # Fusionar por nombre: sumar cantidades y actualizar precio
                for prod_c in inventario_cargado:
                    encontrado = False
                    for prod in inventario:
                        if prod["nombre"].strip().lower() == prod_c["nombre"].strip().lower():
                            prod["cantidad"] += prod_c["cantidad"]
                            prod["precio"] = prod_c["precio"]
                            encontrado = True
                            break
                    if not encontrado:
                        inventario.append(prod_c)
        print(f"Inventario fusionado. Productos cargados: {len(inventario_cargado)}. Filas inválidas omitidas: {errores}")




if __name__ == "__main__":
      main()
