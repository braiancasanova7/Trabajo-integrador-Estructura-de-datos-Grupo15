"""Usuario (el cliente): Es la persona que usa el sistema. 
¿Qué información necesita la oficina de correos para identificarlo? Su nombre, correo y contraseña.
 ¿Qué puede hacer él? Enviar mensajes y autenticarse para entrar a su cuenta.
"""
from Mensaje import Mensaje
class Usuario():
    def __init__(self,nombre,correo,contrasena):
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena
    def enviar_msj(self,destinatario,asunto,cuerpo):
        return Mensaje(self._correo,destinatario,asunto,cuerpo)
   
    def autenticar(self,Verf_correo,Verf_contra):
        #1deberia verificar si existe
        return self._correo == Verf_correo and self._contrasena == Verf_contra
    pass
    def correo(self):
        return self._correo








             
        
    #   def confirmarEnvio_msj(self,mensaje):
    #     #le entrego un objeto Mensaje
    #     if mensaje.self._emisor in self._usuarios:
    #         #coloco el msj en su buzon salida
    #         #busco en el diccionario de buzones

    #         carpetaUsuario = self._buzones[mensaje.self._emisor]
    #         #busco bandeja
    #         salida = carpetaUsuario["Buzon Salida"]
    #         #Agrego en clave Entrada: Valor Mensaje, con metodo()
    #         salida.agregar_msj(mensaje)
        