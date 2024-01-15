
## Invera Challenge -- ToDO List

El Challenge consiste en crear una aplicación que permita a los usuarios crear y mantener una lista de tareas.

Porfavor sigan las instrucciones debajo para instalar y correr el proyecto correctamente.

## Instalación

1. Crear un entorno virtual: `pip install virtualenv [nombre_entorno]` y activarlo.

2. Clonar el repositorio ejecutando el siguiente comando en tu consola `git clone https://github.com/tomastessio/todo-challenge.git`

3. El próximo paso es instalar todas las dependencias ejecutando `pip install -r requirements.txt`

4. Crear las migraciones de los modelos de datos con los comandos `python manage.py makemigrations` y `python manage.py migrate` 

5. Crear un superusuario para la base de datos `python manage.py createsuperuser` y seguir las instrucciones de la consola.


## Correr el proyecto

1. Para levantar el proyecto, ejecutar el comando `python manage.py runserver` y se encontrará funcionando en `http://localhost:8000`.

2. El proyecto ya esta funcionando correctamente, dirigirse a  `http://localhost:8000/swagger/` para explorar la documentación de las API

## Unit Tests

1. Para ejecutar los tests se debe detener el servidor con `Ctrl + C`.

2. Una vez frenado, usar el siguiente comando `python manage.py test` y ver el resultado.

3. Para probar manualmente las API, se recomienda utilizar la UI brindada por Swagger o Postman.
   a. Para probar utilizando Swagger, dirigirse al endpoint de login y brindar las credenciales creadas at supra. Se le retornará un JWT. Luego, para probar cualquier otro endpoint se le solicitará dicho JWT. El mismo se coloca en la pestañana de "Authorize" anteponiendo la palabra Bearer + el JWT.
   b. Para probar utilizando Postman, repetir el procedimiento. La diferencia radica en dirigirse a la pestaña "Authorization" e indicar el tipo de token "Bearer". Pegar el token en la casilla para probar todos los demás endpoints.