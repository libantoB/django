# Gestor de Tareas con Django

Este es un proyecto básico de gestión de tareas desarrollado con Django que permite a los usuarios crear, ver y administrar sus tareas personales.

## Características principales

- Autenticación de usuarios (registro, inicio y cierre de sesión)
- Creación, edición y eliminación de tareas
- Cada tarea incluye:
  - Título
  - Descripción (opcional)
  - Estado (completada/no completada)
  - Fechas de creación y actualización
- Las tareas están asociadas al usuario que las crea
- Interfaz básica con Bootstrap

## Requisitos del sistema

- Python 3.x
- Django 5.1.7 o superior
- pip (para instalar dependencias)

## Instalación

1. Clona el repositorio o descarga los archivos
2. Crea un entorno virtual (recomendado):
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias:
   ```
   pip install django
   ```
5. Aplica las migraciones:
   ```
   python manage.py migrate
   ```
6. Crea un superusuario (opcional, para acceder al admin):
   ```
   python manage.py createsuperuser
   ```
7. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Estructura del proyecto

- `taskmanager/`: Configuración principal del proyecto Django
- `tasks/`: Aplicación que contiene:
  - `models.py`: Define el modelo Task para las tareas
  - `views.py`: Lógica de las vistas (no mostrado en el código)
  - `templates/`: Plantillas HTML (base.html mostrado)
  - `urls.py`: Rutas de la aplicación (no mostrado)

## Configuración

El proyecto viene con configuración básica para desarrollo:
- Base de datos SQLite
- Debug activado
- Secret key generada automáticamente (debes cambiarla para producción)

## Personalización

Puedes modificar:
- `settings.py` para cambiar la configuración
- `base.html` para ajustar el diseño
- El modelo `Task` para añadir más campos

## Uso

1. Accede a la aplicación en `http://localhost:8000`
2. Regístrate o inicia sesión
3. Gestiona tus tareas desde la interfaz

## Notas de seguridad

⚠️ **Para entornos de producción:**
- Cambia la SECRET_KEY
- Establece DEBUG=False
- Configura ALLOWED_HOSTS adecuadamente
- Usa una base de datos más robusta que SQLite
- Implementa HTTPS

## Licencia

Este proyecto está disponible bajo la licencia MIT.
