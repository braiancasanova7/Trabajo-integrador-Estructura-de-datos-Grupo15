from abc import ABC, abstractmethod

class Interfaz_correo(ABC):
    """
    Define la interfaz para las operaciones de correo.
    """
    @abstractmethod
    def enviar_msj(self, destinatario: str, asunto: str, cuerpo: str):
        pass

    @abstractmethod
    def recibir_msj(self) -> str:
        pass

    @abstractmethod
    def eliminar_msj(self):
        pass

    @abstractmethod
    def listar_msg(self, carpeta: 'Carpeta'):
        pass
