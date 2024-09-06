# from gestion_libros.inventario import agregar_libro   
# from gestion_libros.inventario  import inventario
# from gestion_libros.ventas import vender_libro
# from gestion_libros.ventas import ventas
# def mostrar_menu():
#     """muestra el menu principal"""

#     print("\n -- menu de la tienda de libros ---")
#     print("1. agregar libros al inventario")
#     print("2. mostrar inventario")
#     print("3. vender libro")
#     print("4. mostrar total venta")
#     print("5. salir")

    

# def menu():
#     while True:
#         print("1. Agregar libros al inventario")
#         print("2. Mostrar libros")
#         print("3. Vender libros")
#         print("4. Mostrar total venta")
#         print("5. Salir")
#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             agregar_libro()
#         elif opcion == '2':
#             mostrar_libros()
#         elif opcion == '3':
#             vender_libro()
#         elif opcion == '4':
#             mostrar_total_venta()
#         elif opcion == '5':
#             print("Saliendo del programa...")
#             break
#         else:
#             print("Opción no válida, por favor intente de nuevo.")

# def agregar_libro():
#     titulo = input("Ingrese el título del libro: ")
#     autor = input("Ingrese el autor del libro: ")
#     precio = float(input("Ingrese el precio del libro: "))
#     inventario.agregar_libro(titulo, autor, precio)

# def mostrar_libros():
#     libros = inventario.mostrar_libros()
#     for libro in libros:
#         print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']}")

# def vender_libro():
#     titulo = input("Ingrese el título del libro a vender: ")
#     ventas.vender_libro(titulo)

# def mostrar_total_venta():
#     total = ventas.mostrar_total_venta()
#     print(f"Total de ventas: {total}")

# if __name__ == "__main__":
#     menu()


from gestion_libros.inventario import agregar_libro, mostrar_libros
from gestion_libros.ventas import vender_libro, mostrar_total_venta

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n -- menú de la tienda de libros ---")
    print("1. Agregar libros al inventario")
    print("2. Mostrar inventario")
    print("3. Vender libro")
    print("4. Mostrar total venta")
    print("5. Salir")

def menu():
    while True:
        # print("1. Agregar libros al inventario")
        # print("2. Mostrar libros")
        # print("3. Vender libros")
        # print("4. Mostrar total venta")
        # print("5. Salir")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro_usuario()
        elif opcion == '2':
            mostrar_libros_usuario()
        elif opcion == '3':
            vender_libro_usuario()
        elif opcion == '4':
            mostrar_total_venta_usuario()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def agregar_libro_usuario():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    precio = float(input("Ingrese el precio del libro: "))
    agregar_libro(titulo, autor, precio)

def mostrar_libros_usuario():
    libros = mostrar_libros()
    if libros:
        for libro in libros:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']}")
    else:
        print("No hay libros en el inventario.")

def vender_libro_usuario():
    titulo = input("Ingrese el título del libro a vender: ")
    vender_libro(titulo)

def mostrar_total_venta_usuario():
    total = mostrar_total_venta()
    print(f"Total de ventas: {total}")

if __name__ == "__main__":
    menu()
