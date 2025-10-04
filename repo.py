# repo.py
from repo_base import RepoBase

class RepositorioArchivo(RepoBase):
    def __init__(self, ruta="biblioteca.txt"):
        """Recibe la ruta del archivo donde se guardará la info mínima."""
        self.ruta = ruta

    def guardar(self, libros, prestamos):
        """ Guarda conteos simples en el archivo (número de libros y de préstamos). """
        with open(self.ruta, "w", encoding="utf-8") as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")

    def cargar(self):
        """ Lee el archivo y regresa su contenido como texto."""
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""
