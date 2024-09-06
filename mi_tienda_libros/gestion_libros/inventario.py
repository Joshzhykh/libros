

# libros = []

# def agregar_libro(titulo, autor, precio):
#     libro = {'titulo': titulo, 'autor': autor, 'precio': precio}
#     libros.append(libro)

# def mostrar_libros():
#     return libros


libros = []

def agregar_libro(titulo, autor, precio):
    """Agrega un libro al inventario."""
    libro = {'titulo': titulo, 'autor': autor, 'precio': precio}
    libros.append(libro)

def mostrar_libros():
    """Devuelve la lista de libros en el inventario."""
    return libros


# agregar = agregar_libro("ola","yo",100)
# agregar2 = agregar_libro("pop","josh",999)
# print(agregar)
# print(agregar2)

# print(libros)
