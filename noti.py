# noti.py
class ServicioNotificaciones:
    def enviar(self, usuario, titulo_libro):
        """ Muestra en consola una notificación simple del préstamo  """
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{titulo_libro}'")
