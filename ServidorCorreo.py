""" ServidorCorreo (el cartero y la central): Es el corazón del sistema. Se encarga de 
    gestionar a todos los usuarios, saber dónde están sus carpetas y, lo más importante, 
    manejar el envío y la recepción de mensajes entre usuarios.

"""
from Usuario import Usuario
from Carpeta import carpeta
from Mensaje import Mensaje
class GestorCorreo():
       
    def __init__(self):
        self._usuarios = {}
        self._buzones = {}


    def registrar_usuario(self,usuario):
        #uso el objeto Usuario, aqui paso una instancia como argumento usuario
        #uso el diccionario para almacenar una lista de usuarios. Clave=correo; Valor=Usuario. obj-usuario
        if usuario in self._usuarios:
            return f"El usuario {usuario} No puuede registrarse. Ya Esta registrado"
        else:
            #registro usuario con su correo como clave
            self._usuarios[usuario.correo()] = usuario
            #le asigno a usuario su carpetas
            buzon_entrada = carpeta("Entrada")
            buzon_salida = carpeta("Salida")
            self._buzones[usuario.correo()] = {"Buzon Entrada": buzon_entrada, "Buzon Salida": buzon_salida}
            return f"El usuario {usuario} Se Registro con exito"

    def entregar_msj(self,mensaje):
        #le entrego un objeto Mensaje
        if mensaje.self._receptor in self._usuarios:
            #coloco el msj en su buzon entrada
            #busco en el diccionario de buzones

            carpetaUsuario = self._buzones[mensaje.self._receptor]
            #busco bandeja
            Entrada = carpetaUsuario["Buzon Entrada"]
            salida = carpetaUsuario["Buzon Salida"]

            #Agrego en clave Entrada: Valor Mensaje, con metodo()
            Entrada.agregar_msj(mensaje)
            salida.agregar_msj(mensaje)
        else:
            return f"El usuario no esta registrado"