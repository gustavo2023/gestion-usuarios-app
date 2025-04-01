# Pruebas y Tests

Este documento describe las pruebas implementadas en el proyecto "Gestión de Usuarios" y cómo ejecutarlas.

---

## Cómo Ejecutar las Pruebas

Para ejecutar las pruebas, sigue estos pasos:

1. Asegúrate de tener instalado `pytest` en tu entorno virtual. Si no lo tienes, instálalo con:

   ```bash
   pip install pytest
   ```

2. Ejecuta las pruebas desde la raíz del proyecto con el siguiente comando:

    ```bash
    pytest tests/ -v
    ```

    - `tests`: Especifica el directorio donde se encuentran las pruebas.
    - `-v`: Muestra los resultados de las pruebas en modo detallado.

3. Si todas las pruebas pasan, verás un mensaje como este:

    ```bash
    =================== test session starts ===================
    collected 4 items

    tests/test_user_service.py::test_create_user_valid PASSED [ 25%]
    tests/test_user_service.py::test_validate_email PASSED [ 50%]
    tests/test_user_service.py::test_create_user_empty_fields PASSED [ 75%]
    tests/test_user_service.py::test_get_all_users PASSED [100%]

    =================== 4 passed in 0.12s ===================
    ```

A continuación, se describen las pruebas implementadas en el archivo `test_user_service.py`:

1. `test_create_user_valid`:

    - **Descripción:** Verifica que se pueda crear un usuario válido en la base de datos.
    - **Pasos:**

        1. Llama a la función `create_user` con un nombre, correo electrónico y contraseña válidos.
        2. Comprueba que el usuario creado tiene un `id` asignado.

    - **Resultado Esperado:** El usuario se crea correctamente y se le asigna un `id`.

2.  `test_validate_email`

    - **Descripción:** Valida diferentes formatos de correos electrónicos para asegurarse de que la función validate_email funcione correctamente.
    - **Pasos:**

        1. Usa `pytest.mark.parametrize` para probar múltiples casos de correos electrónicos.
        2. Comprueba si la función devuelve `True` para correos válidos y `False` para correos inválidos.

    - **Casos Probados:**

        - `"test@example.com"` → `True`
        - `"invalid-email"` → `False`
        - `"another@bad"` → `False`
        - `"missing@dotcom"` → `False`

    - **Resultado Esperado:** La función identifica correctamente los correos válidos e inválidos.

3. `test_create_user_empty_fields`

    - **Descripción:** Verifica que no se pueda crear un usuario si alguno de los campos requeridos está vacío.
    - **Pasos:**

        1. Llama a la función `create_user` con un campo vacío (por ejemplo, nombre vacío).
        2. Comprueba que se lanza una excepción `ValueError`.
        3. Verifica que el mensaje de error contiene la palabra "obligatorios".

    - **Resultado Esperado:** La función lanza un error indicando que todos los campos son obligatorios.

4. `test_get_all_users`

    - **Descripción:** Verifica que la función `get_all_users` recupere correctamente todos los usuarios de la base de datos.
    - **Pasos:**

        1. Crea dos usuarios en la base de datos utilizando la función `create_user.`
        2. Llama a la función `get_all_users` para recuperar los usuarios.
        3. Comprueba que el número de usuarios recuperados es igual a 2.

    - **Resultado Esperado:** La función devuelve una lista con los dos usuarios creados.

## Notas Adicionales

- **Base de Datos de Pruebas:** Las pruebas utilizan una base de datos SQLite en memoria (`sqlite:///:memory:`) para garantizar que no se modifiquen los datos reales.
- **Recreación del Esquema:** Antes de cada prueba, el esquema de la base de datos se recrea automáticamente para garantizar un entorno limpio.
- **Manejo de Errores:** Las pruebas verifican que las funciones manejen correctamente los errores, como campos vacíos o correos electrónicos inválidos.

## Archivos Relacionados

- [Archivo de Pruebas](../tests/test_user_service.py)
- [Archivo de Servicios](../src/services/user_service.py)
- [Modelo de Usuario](../src/models/user.py)
