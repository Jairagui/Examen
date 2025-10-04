# busca.py
class PorTitulo:
    def buscar(self, libros, valor):
        """
        Devuelve libros cuyo título contiene el valor
        """
        v = str(valor).lower()
        return [l for l in libros if v in l.titulo.lower()]

class PorAutor:
    def buscar(self, libros, valor):
        """
        Devuelve libros cuyo autor contiene el valor
        """
        v = str(valor).lower()
        return [l for l in libros if v in l.autor.lower()]

class PorISBN:
    def buscar(self, libros, valor):
        """Devuelve libros cuyo ISBN coincide exactamente con el valor."""
        return [l for l in libros if l.isbn == str(valor)]

class PorDisponible:
    def buscar(self, libros, valor):
        """ Devuelve libros filtrando por disponibilidad."""
        ok = (str(valor).lower() == "true")
        return [l for l in libros if l.disponible == ok]

class Buscador:
    def __init__(self):
        """ Registra las estrategias disponibles en un diccionario. """
        self.mapa = {
            "titulo": PorTitulo(),
            "autor": PorAutor(),
            "isbn": PorISBN(),
            "disponible": PorDisponible()
        }

    def buscar(self, clave, libros, valor):
        """ Selecciona la estrategia por clave y ejecuta la búsqueda  """
        est = self.mapa.get(clave)
        return est.buscar(libros, valor) if est else []
