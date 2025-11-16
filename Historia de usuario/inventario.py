# Task 2 ingreso de datos

nombre_producto = input("Ingrese el nombre del producto: ")

# Solicitar y validar el precio del producto (float).

precio_unitario = 0.0
while True:
    try:
        entrada_precio = input("Ingrese el precio unitario (): ")
        
        # Convertir la entrada a float
        precio_unitario = float(entrada_precio)
        if precio_unitario >= 0:
             break
        else:
             print("ERROR: El precio debe ser un número positivo.")
    except ValueError:
        
        print("ERROR: Ingrese un valor numérico válido para el precio.")
        
# Solicitar y validar la cantidad del producto (int).

cantidad = 0
while True:
    try:
        entrada_cantidad = input("Ingrese la cantidad en stock (número entero): ")
        # Convertir la entrada a int
        cantidad = int(entrada_cantidad)
        if cantidad >= 0:
            break
        else:
            print("ERROR: La cantidad debe ser un número entero positivo o cero.")
    except ValueError:
        
        print("ERROR: Ingrese un número entero válido para la cantidad.")

# Task 3: Operación matemática (costo total)

# Multiplicar el precio unitario (float) por la cantidad (int) para obtener el costo total.

costo_total = precio_unitario * cantidad

# Task 4: Salida de datos.

print("\n--- Registro exitoso ---")


resultado = f"Producto: {nombre_producto} | Precio: ${precio_unitario:.2f} | Cantidad: {cantidad} unidades | Total: ${costo_total:.2f}"
print(resultado)

print("-------------------------------------------\n")

# TASK 5: Documentación del código (Comentario General)
# -----------------------------------------------------------
# El programa 'inventario.py' ha cumplido con el objetivo de la Semana 1.
# - Registra tres datos obligatorios (nombre, precio, cantidad) con la función input().
# - Utiliza variables de tipo string, float e int.
# - Valida que el precio y la cantidad sean números correctos usando try-except y bucles while.
# - Realiza la operación básica de inventario: costo_total = precio * cantidad.
# - Muestra la salida formateada en la consola con la función print().






