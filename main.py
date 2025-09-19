from src.Usuario import Usuario
from src.gestor_correo import GestorCorreo, ClienteCorreo

def main():
    # Crear un gestor de correo
    gestor = GestorCorreo()

    # Registrar dos usuarios
    usuario1 = Usuario("Usuario Uno", "usuario1@example.com", "contra123")
    usuario2 = Usuario("Usuario Dos", "usuario2@example.com", "contra456")
    gestor.registrar_usuario(usuario1)
    gestor.registrar_usuario(usuario2)

    # Iniciar sesión como usuario1
    cliente1 = None
    if usuario1.autenticar("usuario1@example.com", "contra123"):
        print("Inicio de sesión exitoso para usuario1.")
        cliente1 = ClienteCorreo(usuario1, gestor)
    else:
        print("Error de inicio de sesión para usuario1.")
        return

    # Iniciar sesión como usuario2
    cliente2 = None
    if usuario2.autenticar("usuario2@example.com", "contra456"):
        print("Inicio de sesión exitoso para usuario2.")
        cliente2 = ClienteCorreo(usuario2, gestor)
    else:
        print("Error de inicio de sesión para usuario2.")
        return

    # Usuario1 envía un mensaje a usuario2
    if cliente1:
        print("\nUsuario1 enviando mensaje a usuario2...")
        cliente1.enviar_msj("usuario2@example.com", "Hola desde usuario1", "Este es un mensaje de prueba.")

    # Usuario2 revisa su bandeja de entrada
    if cliente2:
        print("\nUsuario2 revisando su bandeja de entrada...")
        print(cliente2.listar_msg("entrada"))

    # Usuario2 lee el mensaje
    if cliente2:
        print("\nUsuario2 leyendo el mensaje...")
        print(cliente2.recibir_msj())

    # Usuario2 revisa su bandeja de entrada de nuevo
    if cliente2:
        print("\nUsuario2 revisando su bandeja de entrada de nuevo...")
        print(cliente2.listar_msg("entrada"))

    # Usuario1 revisa su carpeta de enviados
    if cliente1:
        print("\nUsuario1 revisando su carpeta de enviados...")
        print(cliente1.listar_msg("enviados"))

if __name__ == "__main__":
    main()
