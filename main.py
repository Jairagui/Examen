# main.py

from valida import ValidadorBiblioteca
from repo import RepositorioArchivo
from noti import ServicioNotificaciones
from biblioteca_examen import SistemaBiblioteca

val = ValidadorBiblioteca()
repo = RepositorioArchivo("biblioteca.txt")
noti = ServicioNotificaciones()

s = SistemaBiblioteca(val, repo, noti)

print(":=== AGREGANDO LIBROS ===")
print(s.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "9780060883287"))
print(s.agregar_libro("El Principito", "Antoine de Saint-Exupéry", "9780156012195"))
print(s.agregar_libro("1984", "George Orwell", "9780451524935"))
print()

print("=== BÚSQUEDA POR AUTOR ===")
res = s.buscar_libro("autor", "García")
for l in res:
    print("-", l.titulo)
print()

print("=== REALIZAR PRÉSTAMO ===")
print(s.realizar_prestamo(1, "Juan Pérez"))
print()

print("=== LIBROS DISPONIBLES ===")
for l in s.obtener_libros_disponibles():
    print("-", l.titulo)
print()

print("=== DEVOLVER LIBRO ===")
print(s.devolver_libro(1))
print()

print("=== PRÉSTAMOS ACTIVOS ===")
print("Total de préstamos activos:", len(s.obtener_prestamos_activos()))
