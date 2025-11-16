# Programa: inventario_semana2.py


# 1. Almacenamiento Global
# -----------------------------------------------------------
# La lista 'inventario' almacenará todos los productos, donde cada producto es un diccionario.
inventario = []

# -----------------------------------------------------------
# TASK 5: Estructurar el código en funciones simples
# -----------------------------------------------------------

def agregar_producto():
    """
    Función que solicita datos al usuario (nombre, precio, cantidad)
    y agrega un nuevo producto (diccionario) a la lista 'inventario'.
    Incluye validación para precio (float) y cantidad (int).
    """
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    # Solicitar nombre (string)
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validar Precio (float)
    precio = 0.0
    while True:
        try:
            # Se usa el código de validación de la Semana 1
            entrada_precio = input("Ingrese el precio unitario: ")
            precio = float(entrada_precio)
            if precio >= 0:
                break
            else:
                print("ERROR: El precio debe ser un número positivo.")
        except ValueError:
            print("ERROR: Ingrese un valor numérico válido para el precio.")

    # Validar Cantidad (int)
    cantidad = 0
    while True:
        try:
            # Se usa el código de validación de la Semana 1
            entrada_cantidad = input("Ingrese la cantidad en stock: ")
            cantidad = int(entrada_cantidad)
            if cantidad >= 0:
                break
            else:
                print("ERROR: La cantidad debe ser un número entero positivo o cero.")
        except ValueError:
            print("ERROR: Ingrese un número entero válido para la cantidad.")

    # TASK 2: Almacenar el producto como un diccionario y añadirlo a la lista
    
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(nuevo_producto)
    print(f"\n Producto '{nombre}' agregado al inventario.")

def mostrar_inventario():
    """
    Función que recorre la lista 'inventario' y muestra cada producto.
    """
    print("\n--- INVENTARIO ACTUAL ---")
    
    # TASK 3: Verificar si el inventario está vacío
    
    if not inventario:
        print("El inventario está vacío. Agregue algun producto primero.")
        return

    # TASK 3: Recorrer el inventario con un bucle for
    for producto in inventario:
        
        # Mostrar detalles del producto
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
    print("-" * 25)

def calcular_estadisticas():
    """
    calcula el valor total del inventario y la cantidad total de productos.
    """
    print("\n--- Estadisticas del inventario ---")

    if not inventario:
        print("El inventario está vacío. No hay estadísticas para mostrar.")
        return

    # TASK 4: Inicializar contadores
    
    valor_total_inventario = 0.0
    cantidad_total_productos = 0

    # TASK 4: Recorrer la lista para calcular la sumatoria
    
    for producto in inventario:
        # Cálculo del costo por producto (precio * cantidad)
        costo_producto = producto["precio"] * producto["cantidad"]
        
        # Sumar al valor total del inventario
        valor_total_inventario += costo_producto
        
        # Sumar a la cantidad total de unidades
        cantidad_total_productos += producto["cantidad"]
        

    # TASK 4: Mostrar resultados de manera clara
    
    
    print(f"Total de Unidades Registradas: {cantidad_total_productos} unidades")
    print(f"Valor Total Estimado del Inventario: ${valor_total_inventario:,.2f}")
    print("-" * 40)

def menu_principal():
    """
    Función principal que ejecuta el bucle while y maneja el menú interactivo.
    """
    # TASK 2: Envuelve el menú en un bucle while que continúa hasta que la opción sea '4'
    while True:
        print("\n==================================")
        print("        MENÚ DE INVENTARIO        ")
        print("==================================")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("----------------------------------")

        # Leer la opción elegida por el usuario
        
        opcion = input("Seleccione una opción (1-4): ")

        # TASK 1: Usar condicionales if/elif/else para procesar la opción
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            calcular_estadisticas()
        elif opcion == '4':
            print("\n ¡Gracias por usar el sistema de inventario! Saliendo...")
            break # Salir del bucle while
        else:
            # TASK 1: Manejar opción inválida
            print("\n ERROR: Opción no válida. Por favor, ingrese un número del 1 al 4.")


# Ejecución del programa

if __name__ == "__main__":
    menu_principal()

# -----------------------------------------------------------
# TASK 5: Comentario Final
# -----------------------------------------------------------
# Resumen Semana 2: Este programa utiliza el control de flujo y estructuras de datos avanzadas.
# Se implementó un bucle 'while' con un menú interactivo. Se usan 'if/elif/else' para
# la navegación y validación de opciones. Los productos se almacenan como diccionarios
# dentro de una lista global, y se usa un bucle 'for' para recorrer y calcular estadísticas
# como el valor total y la cantidad total de unidades. El código está modularizado en funciones.