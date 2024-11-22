# test.py
from biblioteca import Biblioteca

if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    print(biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez"))
    print(biblioteca.agregar_libro("El Principito", "Antoine de Saint-Exupéry"))

    # Listar libros
    print("\nLibros en la biblioteca:")
    print(biblioteca.listar_libros())

    # Buscar un libro
    print("\nBuscar libro:")
    print(biblioteca.buscar_libro("Cien años de soledad"))
    print(biblioteca.buscar_libro("El túnel"))
