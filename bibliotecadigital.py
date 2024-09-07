# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(título='{self.info[0]}', autor='{self.info[1]}', categoría='{self.categoria}', ISBN='{self.isbn}')"


# Clase Usuario
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []  # Lista de libros prestados

    def __repr__(self):
        return f"Usuario(ID={self.id_usuario}, nombre='{self.nombre}', libros_prestados={self.libros_prestados})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.historial_prestamos = []  # Lista de préstamos realizados

    # Añadir libro a la biblioteca
    def anadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")

    # Eliminar libro de la biblioteca
    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    # Eliminar usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado de la biblioteca.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Prestar libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
        else:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)  # Remover libro de disponibles
            usuario.libros_prestados.append(libro)  # Añadir libro a la lista de préstamos del usuario
            self.historial_prestamos.append((id_usuario, isbn))
            print(f"El libro '{libro.info[0]}' ha sido prestado a {usuario.nombre}.")

    # Devolver libro a la biblioteca
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        else:
            usuario = self.usuarios_registrados[id_usuario]
            libro_a_devolver = None
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    libro_a_devolver = libro
                    break
            if libro_a_devolver:
                usuario.libros_prestados.remove(libro_a_devolver)  # Remover de la lista del usuario
                self.libros_disponibles[isbn] = libro_a_devolver  # Añadir libro de nuevo a la biblioteca
                print(f"El libro '{libro_a_devolver.info[0]}' ha sido devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print(f"Libros encontrados ({criterio}: {valor}):")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros para el criterio '{criterio}' con valor '{valor}'.")

    # Listar libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        else:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados en este momento.")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "67890")

    # Añadir libros a la biblioteca
    biblioteca.anadir_libro(libro1)
    biblioteca.anadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("001", "Juan Pérez")
    biblioteca.registrar_usuario(usuario1)

    # Prestar un libro
    biblioteca.prestar_libro("001", "12345")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")

    # Devolver el libro
    biblioteca.devolver_libro("001", "12345")

    # Buscar libros por título
    biblioteca.buscar_libros("titulo", "Cien años")
