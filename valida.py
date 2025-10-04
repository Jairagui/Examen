# valida.py

class ValidadorBiblioteca:
    def validar_libro(self, titulo, autor, isbn):
        """    Revisa que el título, autor e ISBN sean razonables.  """
        if not titulo or len(titulo) < 2:
            return "Error: Título inválido"
        if not autor or len(autor) < 3:
            return "Error: Autor inválido"
        if not isbn or len(isbn) < 10:
            return "Error: ISBN inválido"
        return None

    def validar_usuario(self, usuario):
        """  Revisa que el nombre de usuario tenga mínimo 3 caracteres.   """
        if not usuario or len(usuario) < 3:
            return "Error: Nombre de usuario inválido"
        return None
