class Mensaje:
    """
    Representa un mensaje de correo electrónico.
    """
    def __init__(self, emisor: str, receptor: str, asunto: str, cuerpo: str):
        self._emisor = emisor
        self._receptor = receptor
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._leido = False

    def ver_mensaje(self) -> str:
        """
        Retorna el contenido completo del mensaje y lo marca como leído.
        """
        self._leido = True
        return f"De: {self._emisor}\nPara: {self._receptor}\nAsunto: {self._asunto}\n\n{self._cuerpo}"

    def msj_resumido(self) -> str:
        """
        Retorna un resumen del mensaje.
        """
        leido_estado = " (Leído)" if self._leido else " (No Leído)"
        return f"De: {self._emisor}, Asunto: {self._asunto}{leido_estado}"

    def get_receptor(self) -> str:
        return self._receptor

    def get_emisor(self) -> str:
        return self._emisor
