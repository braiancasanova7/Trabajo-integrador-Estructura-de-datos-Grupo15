1. Desafíos Iniciales y Razonamiento
Al comenzar, el principal desafío fue entender cómo las diferentes clases interactuarían entre sí. La consigna establece que el sistema debe modelar a un 

Usuario, un Mensaje, una Carpeta, y un ServidorCorreo. Sin embargo, la interconexión entre estas clases no era evidente desde el principio.

Duda: Si la clase Usuario envía un mensaje, ¿debe crear directamente una instancia de la clase Mensaje? ¿Y a quién se la entrega?

Decisión de Diseño: La clase ServidorCorreo se convirtió en el centro de control del sistema. El Usuario crea el objeto Mensaje, pero delega la tarea de "enviarlo" al ServidorCorreo, que actúa como intermediario. Esta decisión nos permitió separar responsabilidades, un pilar fundamental de la programación orientada a objetos (POO).

2. Decisiones de Diseño Clave y su Justificación
Cada decisión de diseño se tomó para garantizar la 

modularidad, la eficiencia y la robustez del sistema, tal como lo requiere la consigna.

Encapsulamiento de Atributos:

¿Qué hicimos? Todos los atributos de las clases (_nombre, _correo, _contenido, etc.) se declararon como privados, utilizando el prefijo de guion bajo (_).

Justificación: Esto protege la integridad de los datos. Otros objetos no pueden modificar directamente los atributos de un Usuario o un Mensaje, evitando inconsistencias. Para acceder a ellos de manera controlada, se crearon métodos o propiedades públicas (@property) que solo devuelven el valor, pero no permiten su modificación directa. Esto permite una validación centralizada de datos.

Uso de Diccionarios Anidados en el ServidorCorreo:

¿Qué hicimos? Decidimos usar diccionarios en la clase ServidorCorreo para almacenar a los usuarios y sus buzones. La clave para ambos diccionarios es la dirección de correo única del usuario. Por ejemplo: 

_usuarios["email"] = objeto Usuario y _buzones["email"] = {"entrada": objeto Carpeta, ...}.

Justificación: Esta estructura de datos fue elegida por su eficiencia. Permite búsquedas directas y rápidas (con una complejidad O(1) en promedio) para verificar si un usuario existe o para encontrar su buzón. Si hubiéramos usado listas, tendríamos que recorrer cada elemento para encontrar al usuario, lo que sería ineficiente a medida que el número de usuarios crezca.

Asignación de Carpetas:

¿Qué hicimos? La creación de las carpetas por defecto ("Entrada" y "Enviados") se realiza de forma automática y se le asigna al usuario en el método registrar_usuario de la clase ServidorCorreo. Cada usuario recibe sus propias instancias de la clase Carpeta.

Justificación: Esto asegura que la lógica de configuración inicial del usuario esté centralizada en una sola clase (ServidorCorreo). Además, al darle a cada usuario su propio conjunto de objetos Carpeta, evitamos tener "carpetas generales" y mantenemos la información organizada y específica para cada cuenta.

Modularidad del Código:

¿Qué hicimos? Separamos cada clase (Usuario, Mensaje, Carpeta, ServidorCorreo) en un archivo de Python independiente (.py).

Justificación: Esta práctica facilita el trabajo en equipo, la lectura del código y el mantenimiento a largo plazo. Al dividir el proyecto en módulos, cada archivo se enfoca en una sola responsabilidad, cumpliendo con los principios de buenas prácticas de programación.

3. Conclusión y Próximos Pasos
La primera entrega se centró en sentar las bases de un sistema robusto, con un diseño de clases y relaciones bien definido. Las decisiones de diseño tomadas, como el uso del 

ServidorCorreo como orquestador y los diccionarios para una gestión eficiente, nos preparan para las próximas etapas del trabajo, donde se agregarán funcionalidades más complejas como árboles y grafos, de acuerdo con la consigna