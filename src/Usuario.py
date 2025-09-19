from typing import Optional

class Usuario:
    """
    Representa un usuario del sistema de correo.
    """
    def __init__(self, nombre: str, correo: str, contrasena: str):
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena

    def enviar_msj(self, destinatario: str, asunto: str, cuerpo: str) -> 'Mensaje':
        """
        Crea y retorna un nuevo mensaje.
        """
        from .Mensaje import Mensaje
        return Mensaje(self._correo, destinatario, asunto, cuerpo)

    def autenticar(self, verf_correo: str, verf_contra: str) -> bool:
        """
        Verifica las credenciales del usuario.
        """
        return self._correo == verf_correo and self._contrasena == verf_contra

    def correo(self) -> str:
        """
        Retorna la dirección de correo del usuario.
        """
        return self._correo
