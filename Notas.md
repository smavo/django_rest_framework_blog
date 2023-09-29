
# Instalaciones

## Crear entorno virtual para el proyecto
```python -m venv venv```

## Install Django 4.2.4
```pip install django==4.2.4```

## Crear proyecto en Django en la carpeta raiz
```django-admin startproject <nombre_proyecto> . ```

## Crear nuevo app
```python manage.py startapp <app_name>```

## Add Django Rest Framework
```pip install djangorestframework```

## Add drf-yasg
```pip install drf-yasg```

## Renderizar archivos estaticos
```python manage.py collectstatic```


## Cambiar el modelo User
* 1. Eliminar las migraciones del proyecto
* 2. Eliminar base de datos 
* 3. Crear el modelo User por defecto
* 4. Volver a correr las migraciones

## Crear usuario
```python manage.py createsuperuser```