
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

2. El proyecto ya esta funcionando correctamente, dirigirse a  `http://localhost:8000/swagger/`.