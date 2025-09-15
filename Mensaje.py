"""
Mensaje (la carta): Es la información que se envía. ¿Qué tiene una carta?
 Un remitente, un destinatario, un asunto, el contenido y, quizás, una marca que dice si ya fue leída.
"""

class Mensaje():
    def __init__(self,emisor,receptor,asunto,cuerpo):
        self._emisor = emisor
        self._receptor = receptor
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._leido = False
    
    def ver_mensaje(self):
        
        return f"Remitente: {self._emisor} Destinatario: {self._receptor} Asunto: {self._asunto}  Mensaje: {self._cuerpo} "
    
    def msj_resumido(self):
        return f"Remitente: {self._emisor}  Asunto: {self._asunto}"