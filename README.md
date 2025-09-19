# Trabajo-integrador-Estructura-de-datos-Grupo15

# Informe Técnico: Diseño de un Sistema de Gestión de Correo Electrónico

## Resumen del Proyecto

El presente informe detalla el diseño de un **Sistema de Gestión de Correo Electrónico** basado en un modelo de clases modular y escalable. El objetivo es simular las funcionalidades clave de un cliente de email, incluyendo la gestión de usuarios, el envío y la recepción de mensajes. La arquitectura propuesta se centra en la clara separación de responsabilidades entre los componentes principales.

---

## Justificación del Diseño Orientado a Objetos

La elección de un enfoque orientado a objetos permite una representación directa y lógica de las entidades del mundo real (usuarios, mensajes y carpetas). Cada clase tiene una responsabilidad única y bien definida, lo que facilita la comprensión, el desarrollo y el mantenimiento del sistema. Este diseño promueve la cohesión y reduce el acoplamiento entre los módulos.

---

## Arquitectura del Sistema

La estructura se compone de las siguientes clases principales, organizadas para manejar la lógica del negocio, el almacenamiento de datos y la interacción con el usuario.

### 1. Entidades del Dominio

* **`Usuario`**: Define las propiedades y comportamientos de un usuario, como la autenticación y la capacidad de enviar mensajes.
* **`Mensaje`**: Contiene la estructura de un correo electrónico (remitente, destinatario, asunto, etc.).
* **`Carpeta`**: Actúa como un contenedor de mensajes, permitiendo organizar los correos de un usuario.

### 2. Capa de Lógica de Negocio

* **`GestorCorreo`**: Centraliza la lógica del servidor de correo. Su responsabilidad es registrar usuarios, almacenar sus datos y buzones, y gestionar la entrega de mensajes entre ellos. Esta clase desacopla la lógica de negocio de las entidades individuales.

### 3. Capa de Interfaz

* **`Interfaz_correo`**: Una clase abstracta que define el contrato para la interacción con el usuario. Promueve la flexibilidad, ya que permite que futuras implementaciones de la interfaz (por ejemplo, una interfaz gráfica o web) sigan la misma estructura.
* **`UsuarioMain`**: La implementación concreta de la interfaz, encargada de manejar la entrada y salida de datos a nivel de la línea de comandos, actuando como el punto de inicio del programa.

---

## Relaciones entre Clases

Las interacciones entre los componentes se definen a través de las siguientes relaciones:

* **Composición (`o--`)**: Una **`Carpeta`** está compuesta por **`Mensaje`s**. La vida de los mensajes está ligada a la carpeta que los contiene.
* **Asociación (`-->`)**: Un **`Usuario`** está asociado a muchas **`Carpeta`s** y a muchos **`Mensaje`s** (que envía). Un **`GestorCorreo`** administra a muchos **`Usuario`s** y contiene las **`Carpeta`s** de los buzones.
* **Generalización (`..|>`)**: **`UsuarioMain`** es una implementación especializada de la clase abstracta **`Interfaz_correo`**.

Este diseño proporciona una base sólida para una implementación funcional, escalable y fácil de mantener.
