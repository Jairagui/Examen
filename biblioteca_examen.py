# biblioteca_examen.py
# Clase central que coordina el flujo

from busca import Buscador
from valida import ValidadorBiblioteca
from noti import ServicioNotificaciones
from repo_base import RepoBase

class Libro:
    def __init__(self, id, titulo, autor, isbn):
        """Modelo de Libro """
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Prestamo:
    def __init__(self, id, libro, usuario):
        """Modelo de Préstamo """
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.activo = True

class SistemaBiblioteca:
    def __init__(self, validador=None, repo: RepoBase=None, noti=None):

        self.libros = []
        self.prestamos = []
        self.contador_libro = 1
        self.contador_prestamo = 1

        # Inyección de dependencias
        self.valida = validador or ValidadorBiblioteca()
        self.repo = repo
        self.noti = noti or ServicioNotificaciones()

        # Buscador de estrategias
        self.bus = Buscador()

    def agregar_libro(self, titulo, autor, isbn):

        err = self.valida.validar_libro(titulo, autor, isbn)
        if err:
            return err

        libro = Libro(self.contador_libro, titulo, autor, isbn)
        self.libros.append(libro)
        self.contador_libro += 1

        if self.repo:
            self.repo.guardar(self.libros, self.prestamos)

        return f"Libro '{titulo}' agregado exitosamente"

    def realizar_prestamo(self, libro_id, usuario):

        err = self.valida.validar_usuario(usuario)
        if err:
            return err

        for libro in self.libros:
            if libro.id == libro_id and libro.disponible:
                libro.disponible = False
                prestamo = Prestamo(self.contador_prestamo, libro, usuario)
                self.prestamos.append(prestamo)
                self.contador_prestamo += 1

                if self.repo:
                    self.repo.guardar(self.libros, self.prestamos)

                self.noti.enviar(usuario, libro.titulo)
                return f"Préstamo realizado a {usuario}"

        return "No se pudo realizar el préstamo"

    def devolver_libro(self, prestamo_id):

        for p in self.prestamos:
            if p.id == prestamo_id and p.activo:
                p.activo = False
                p.libro.disponible = True

                if self.repo:
                    self.repo.guardar(self.libros, self.prestamos)

                return "Libro devuelto exitosamente"

        return "Préstamo no encontrado o ya devuelto"

    def obtener_todos_libros(self):
        """Devuelve la lista completa de libros """
        return self.libros

    def obtener_libros_disponibles(self):
        """Devuelve solo los libros """
        return [l for l in self.libros if l.disponible]

    def obtener_prestamos_activos(self):
        """Devuelve la lista de préstamos que siguen activos """
        return [p for p in self.prestamos if p.activo]

    def buscar_libro(self, clave, valor):

        return self.bus.buscar(clave, self.libros, valor)
