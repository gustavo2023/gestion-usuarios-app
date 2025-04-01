# Explicación del Código

Este documento describe las funciones, métodos y clases principales de los archivos más importantes del proyecto "Gestión de Usuarios".

---

## Archivo: [`main.py`](../src/cli/main.py)

Este archivo contiene la lógica principal de la aplicación de línea de comandos, incluyendo el menú interactivo y las funciones para crear y listar usuarios.

### Funciones

1. **`show_menu()`**
   - Muestra el menú principal de la aplicación.
   - Permite al usuario seleccionar entre las opciones:
     - Crear usuario.
     - Listar usuarios.
     - Salir del programa.

2. **`create_user_cli()`**
   - Permite al usuario crear un nuevo usuario.
   - Solicita el nombre, correo electrónico y contraseña.
   - Valida el nombre para que solo contenga letras y espacios.
   - Llama a la función `create_user` del archivo `user_service.py` para guardar el usuario en la base de datos.

3. **`list_users_cli()`**
   - Recupera y muestra todos los usuarios registrados en la base de datos.
   - Utiliza la biblioteca `rich` para mostrar los datos en una tabla interactiva.

4. **`validate_name(name: str) -> bool`**
   - Valida que el nombre ingresado solo contenga letras, espacios y caracteres acentuados.
   - Devuelve `True` si el nombre es válido, de lo contrario `False`.

5. **`get_db()`**
   - Context manager que proporciona una sesión de base de datos.
   - Garantiza que la conexión a la base de datos se cierre correctamente después de su uso.

---

## Archivo: [`user.py`](../src/models/user.py)

Este archivo define el modelo de datos para la tabla `usuarios` en la base de datos.

### Clase

1. **`User`**
   - Representa la tabla `usuarios` en la base de datos.
   - **Atributos**:
     - `id`: Identificador único del usuario (clave primaria).
     - `nombre`: Nombre del usuario (cadena de hasta 50 caracteres, no nulo).
     - `email`: Correo electrónico único del usuario (cadena de hasta 100 caracteres, no nulo).
     - `password`: Contraseña encriptada del usuario (cadena de hasta 100 caracteres, no nulo).
     - `fecha_creacion`: Fecha y hora de creación del registro (se genera automáticamente).

---

## Archivo: [`connection.py`](../src/database/connection.py)

Este archivo configura la conexión a la base de datos utilizando SQLAlchemy.

### Componentes

1. **`DB_URL`**
   - Obtiene la URL de conexión a la base de datos desde el archivo `.env`.

2. **`engine`**
   - Instancia de SQLAlchemy Engine que gestiona la conexión a la base de datos.
   - Configura un pool de conexiones con un tamaño máximo de 10 y un tiempo de reciclaje de 3600 segundos.

3. **`SessionLocal`**
   - Crea sesiones de base de datos para interactuar con la base de datos.

4. **`Base`**
   - Clase base declarativa utilizada para definir modelos ORM.

---

## Archivo: [`user_service.py`](../src/services/user_service.py)

Este archivo contiene las funciones de servicio para interactuar con la base de datos relacionadas con los usuarios.

### Funciones

1. **`create_user(db: Session, nombre: str, email: str, password: str)`**
   - Crea un nuevo usuario en la base de datos.
   - Valida que el nombre y el correo electrónico sean válidos.
   - Encripta la contraseña antes de guardarla.
   - Lanza excepciones si los datos son inválidos o si el correo electrónico ya está registrado.

2. **`get_all_users(db: Session)`**
   - Recupera todos los usuarios registrados en la base de datos.
   - Devuelve una lista de objetos `User`.

3. **`validate_email(email: str) -> bool`**
   - Valida que el correo electrónico tenga un formato válido.

4. **`validate_name(name: str) -> bool`**
   - Valida que el nombre solo contenga letras y espacios.

5. **`transactional(func)`**
   - Decorador que asegura que las transacciones de base de datos se confirmen (`commit`) o se reviertan (`rollback`) en caso de error.

---

## Archivo: [`logger.py`](../src/utils/logger.py)

Este archivo configura el sistema de logging para registrar eventos importantes en la aplicación.

### Componentes

1. **`logging.basicConfig()`**
   - Configura el formato y el nivel de los logs.
   - Nivel predeterminado: `INFO`.
   - Formato: Incluye la fecha, el nombre del logger, el nivel del log y el mensaje.

2. **`logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)`**
   - Reduce el nivel de los logs de SQLAlchemy a `WARNING` para evitar mensajes innecesarios en la consola.

3. **`logger`**
   - Instancia del logger principal utilizada en todo el proyecto para registrar eventos.

---

## Notas Finales

- Cada archivo está diseñado para cumplir con una responsabilidad específica, siguiendo el principio de separación de responsabilidades.
- El uso de SQLAlchemy y `rich` mejora la interacción con la base de datos y la presentación de datos en la consola.
- El sistema de logging facilita el monitoreo y la depuración del proyecto.
