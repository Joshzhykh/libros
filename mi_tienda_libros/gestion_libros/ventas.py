# from gestion_libros import inventario
# # import main


# ventas = []

# def vender_libro(titulo):
#     for libro in inventario.libros:
#         if libro['titulo'] == titulo:
#             ventas.append(libro['precio'])
#             inventario.libros.remove(libro)
#             print(f"Libro '{titulo}' vendido.")
#             return
#     print(f"Libro '{titulo}' no encontrado en el inventario.")

# def mostrar_total_venta():
#     return sum(ventas)



from gestion_libros.inventario import libros

ventas = []

def vender_libro(titulo):
    """Vende un libro y actualiza el total de ventas."""
    global ventas  # Para asegurarnos de que estamos modificando la variable global
    global libros  # Para modificar la lista de libros en inventario
    
    for libro in libros:
        if libro['titulo'] == titulo:
            ventas.append(libro['precio'])
            libros.remove(libro)
            print(f"Libro '{titulo}' vendido.")
            return
    print(f"Libro '{titulo}' no encontrado en el inventario.")

def mostrar_total_venta():
    """Muestra el total de ventas."""
    return sum(ventas)
