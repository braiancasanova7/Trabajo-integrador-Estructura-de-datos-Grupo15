from typing import List

class Carpeta:
    """
    Representa una carpeta para almacenar mensajes.
    """
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._contenido: List['Mensaje'] = []

    def agregar_msj(self, mensaje: 'Mensaje'):
        """
        Añade un mensaje a la carpeta.
        """
        self._contenido.append(mensaje)

    def get_contenido(self) -> List['Mensaje']:
        """
        Retorna la lista de mensajes en la carpeta.
        """
        return self._contenido

    def get_nombre(self) -> str:
        """
        Retorna el nombre de la carpeta.
        """
        return self._nombre
