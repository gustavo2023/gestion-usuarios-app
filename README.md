# Gestión de Usuarios

Este proyecto es una aplicación de línea de comandos para gestionar usuarios. Permite crear usuarios, listar usuarios y validar datos como correos electrónicos.

---

## Tabla de Contenidos

1. [Características](#características)
2. [Configuración del Proyecto](#configuración-del-proyecto)
3. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)
4. [Capturas de Pantalla](#capturas-de-pantalla)
   - [Menú Principal](#menú-principal)
   - [Crear Usuario](#crear-usuario)
   - [Listar Usuarios](#listar-usuarios)
   - [Registros de la Base de Datos](#registros-de-la-base-de-datos)
5. [Video de Demostración](#video-de-demostración)
6. [Documentación Adicional](#documentación-adicional)

---

## Características

- Crear usuarios con validación de datos.
- Listar usuarios en una tabla interactiva.
- Validación de correos electrónicos y contraseñas.

## Configuración del Proyecto

**1. Clona el repositorio:**

```bash
    git clone https://github.com/tu-usuario/gestion-usuarios.git
    cd gestion-usuarios
```

**2. Crea un entorno virtual:**

```bash
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate
```

**3. Instala las dependencias:**

```bash
    pip install -r requirements.txt
```

**4. Configura la base de datos:**

Los pasos son los siguientes:

- Asegúrate de tener [XAMPP](https://www.apachefriends.org/) y ejecutando MySQL.
- Ingresa al navegador y escribe `localhost`.
- Ingresa en `phpMyAdmin`.
- Crea una base de datos llamada `gestion_usuarios` haciendo clic en el botón `new`.

### Opción 1: Crear la base de datos desde cero

1. Utiliza el [Diagrama ER](./docs/database_er_diagram.md) para crear la tabla `usuarios` con las columnas correspondientes.

### Opción 2: Importar la base de datos desde un archivo .sql

1. Haz clic en la pestaña `Import`.
2. Haz clic en el botón `Choose File` y selecciona el archivo [`gestiond_usuarios.sql`](./docs/gestion_usuarios.sql) ubicado en el directorio `docs` del proyecto.
3. Haz clic en el botón `Import` en la parte inferior de la página.

Finalmente:

- Configura el archivo `.env` con la URL de conexión:

  `DB_URL=mysql+mysqlconnector://root:@localhost:3306/gestion_usuarios`

**5. Instala el proyecto en modo editable:**

```bash
    pip install -e
```

## Cómo Ejecutar el Proyecto

**1. Ejecuta el siguiente comando para iniciar la aplicación:**

```bash
    python src/cli/main.py
```

**2. Interactúa con el menú:**

- Opción 1: Crear usuario.
- Opción 2: Listar usuarios.
- Opción 3: Salir.

## Capturas de Pantalla

### Menú Principal

![Menú Principal](./screenshots/menu_principal.png)

### Crear Usuario

![Crear Usuario Parte 1](./screenshots/crear_usuario_1.png)
![Crear Usuario Parte 2](./screenshots/crear_usuario_2.png)

### Listar Usuarios

![Listar Usuarios](./screenshots/listar_usuarios.png)

### Registros de la Base de Datos

![Registros en la Base de Datos](./screenshots/registros_base_datos.png)

## Video de Demostración

A continuación, se muestra un video de demostración del programa en funcionamiento:

[![Ver Video](./screenshots/video_thumbnail.png)](https://drive.google.com/file/d/1CnRohmsIGHoNzJ6yvsJGJKLbNa814eeE/view?usp=drive_link)

Haz clic en la imágen para ver el video

## Documentación Adicional

- [Diagrama ER de la Base de Datos](docs/database_er_diagram.md)
- [Explicación del Código](docs/code_explanation.md)
- [Pruebas y Tests](docs/tests.md)
