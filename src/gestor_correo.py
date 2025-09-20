from typing import Dict, List
from .Usuario import Usuario
from .Mensaje import Mensaje
from .Carpeta import Carpeta
from .interfaz_correo import Interfaz_correo

class GestorCorreo:
    """
    Clase principal que gestiona los usuarios y el flujo de mensajes.
    """
    def __init__(self):
        self._usuarios: Dict[str, Usuario] = {}
        self._buzones: Dict[str, Dict[str, Carpeta]] = {}

    def registrar_usuario(self, usuario: Usuario):
        """
        Registra un nuevo usuario en el sistema.
        """
        if usuario.correo() not in self._usuarios:
            self._usuarios[usuario.correo()] = usuario
            self._buzones[usuario.correo()] = {
                "entrada": Carpeta("entrada"),
                "enviados": Carpeta("enviados")
            }
            print(f"Usuario {usuario.correo()} registrado con éxito.")
        else:
            print(f"El usuario {usuario.correo()} ya existe.")

    def entregar_msj(self, mensaje: Mensaje):
        """
        Entrega un mensaje al buzón del receptor.
        """
        receptor_correo = mensaje.get_receptor()
        emisor_correo = mensaje.get_emisor()

        if receptor_correo in self._buzones:
            self._buzones[receptor_correo]["entrada"].agregar_msj(mensaje)
            print(f"Mensaje entregado a {receptor_correo}.")
        else:
            print(f"No se pudo entregar el mensaje. Usuario {receptor_correo} no existe.")

        # Mueve el mensaje a la carpeta de 'enviados' del emisor.
        if emisor_correo in self._buzones:
            self._buzones[emisor_correo]["enviados"].agregar_msj(mensaje)

# Añado una clase que implementa la interfaz
class ClienteCorreo(Interfaz_correo):
    def __init__(self, usuario: Usuario, gestor_correo: GestorCorreo):
        self._usuario = usuario
        self._gestor = gestor_correo

    def enviar_msj(self, destinatario: str, asunto: str, cuerpo: str):
        nuevo_mensaje = self._usuario.enviar_msj(destinatario, asunto, cuerpo)
        self._gestor.entregar_msj(nuevo_mensaje)

    def recibir_msj(self) -> str:
        # Esto sería una lógica más compleja en un sistema real.
        # Por ahora, se mostrará el último mensaje de la bandeja de entrada.
        carpeta_entrada = self._gestor._buzones[self._usuario.correo()]["entrada"]
        mensajes_entrada = carpeta_entrada.get_contenido()
        if mensajes_entrada:
            ultimo_mensaje = mensajes_entrada[-1]
            return ultimo_mensaje.ver_mensaje()
        return "No hay mensajes nuevos."

    def eliminar_msj(self):
        print("Función de eliminación no implementada en este ejemplo.")

    def listar_msg(self, carpeta_nombre: str) -> str:
        carpeta_seleccionada = self._gestor._buzones[self._usuario.correo()].get(carpeta_nombre)
        if not carpeta_seleccionada:
            return f"Carpeta '{carpeta_nombre}' no encontrada."

        resumen_mensajes = [msj.msj_resumido() for msj in carpeta_seleccionada.get_contenido()]
        if not resumen_mensajes:
            return f"La carpeta '{carpeta_nombre}' está vacía."

        return "\n".join(resumen_mensajes)
