"""
Carpeta (el archivador): Es donde guardas tus mensajes, como la bandeja de entrada
 o la de spam. Una carpeta tiene un nombre (por ejemplo, "Recibidos") y una lista de
   mensajes que contiene. Puede agregar o eliminar mensajes.
"""

class carpeta():
    def __init__(self, nombre):
        self._nombre = nombre
        self._contenido = []
    
    def agregar_msj(self,mensaje):
        self._contenido.append(mensaje)

    
    def listar_msj(self):
        pass