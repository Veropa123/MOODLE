# -*- coding: utf-8 -*-
from copy import deepcopy

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre (sin distinción de mayúsculas) y retorna la
    referencia al diccionario en la lista si lo encuentra, o None si no.
    """
    nombre_limpio = nombre.strip().lower()
    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre_limpio:
            return producto
    return None

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto. Si ya existe, actualiza la cantidad sumando la nueva
    y sobrescribe el precio con el más reciente.
    """
    producto_existente = buscar_producto(inventario, nombre)
    
    if producto_existente:
        # Si existe, actualiza cantidad y precio
        producto_existente["cantidad"] += cantidad
        producto_existente["precio"] = precio
        return True # Devuelve True para indicar que se actualizó
    else:
        # Si no existe, lo añade a la lista
        inventario.append({"nombre": nombre.strip(), "precio": precio, "cantidad": cantidad})
        return True

def mostrar_inventario(inventario):
    """
    Muestra todos los productos en el inventario de forma formateada.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
        
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'NOMBRE':<30} | {'PRECIO':>10} | {'CANTIDAD':>8}")
    print("-" * 52)
    for p in inventario:
        # Usamos :.2f para asegurar que el precio se muestre con dos decimales
        print(f"{p['nombre']:<30} | ${p['precio']:>9.2f} | {p['cantidad']:>8}")
    print("-" * 52)
    print(f"Total de productos distintos: {len(inventario)}")

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False
        
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
        
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
        
    return True

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre y retorna True/False.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        # Eliminamos el producto de la lista (ya que buscar_producto retorna la referencia)
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    """
    Calcula el valor total, unidades y encuentra el producto más caro y con mayor stock.
    Retorna un diccionario de estadísticas o None si el inventario está vacío.
    """
    if not inventario:
        return None
        
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    
    # deepcopy es crucial aquí para que la lista de inventario no se modifique externamente.
    producto_mas_caro = deepcopy(max(inventario, key=lambda p: p["precio"]))
    producto_mayor_stock = deepcopy(max(inventario, key=lambda p: p["cantidad"]))
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

def fusionar_inventarios(inventario_destino, inventario_fuente):
    """
    Fusiona productos de inventario_fuente al inventario_destino.
    Si el producto existe, suma la cantidad y actualiza el precio.
    Si no existe, lo agrega.
    
    Retorna la lista fusionada (una nueva lista con los productos de destino).
    """
    # Creamos una copia profunda para trabajar y no afectar los originales.
    inventario_fusionado = deepcopy(inventario_destino)
    
    for producto_nuevo in inventario_fuente:
        nombre_nuevo_limpio = producto_nuevo["nombre"].strip().lower()
        encontrado = False
        
        for producto_existente in inventario_fusionado:
            if producto_existente["nombre"].strip().lower() == nombre_nuevo_limpio:
                # Si existe, fusionar: sumar cantidad, actualizar precio.
                producto_existente["cantidad"] += producto_nuevo["cantidad"]
                # Se queda con el precio del archivo fuente, que puede ser el más reciente
                producto_existente["precio"] = producto_nuevo["precio"] 
                encontrado = True
                break
        
        if not encontrado:
            # Si no existe, añadir el producto a la lista fusionada.
            inventario_fusionado.append(deepcopy(producto_nuevo))
            
    return inventario_fusionado