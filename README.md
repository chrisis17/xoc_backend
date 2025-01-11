# Django Backend Project  

Este proyecto es un backend desarrollado con Django. A continuación, encontrarás las instrucciones necesarias para instalar y ejecutar el proyecto en tu máquina local.  

---

## **Requisitos previos**  
Antes de comenzar, asegúrate de tener instalados los siguientes elementos:  
- [Python](https://www.python.org/downloads/) (versión 3.6 o superior).  
- [Pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python).  

Para comprobar si ya los tienes instalados, puedes ejecutar los siguientes comandos:  

```bash
python --version
pip --version

```
### Paso 1: Clonar este repositorio 
```bash
git clone https://github.com/chrisis17/xoc_backend.git
```

### Paso 2: Instalar requerimientos necesarios
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar servidor
```bash
python manage.py runserver
```

LISTO! El backend estará corriendo en el servidor local: localhost:8000

# Rutas de comunicación API
A continuación se explicarán las rutas requeridas para la comunicación REST

## http://127.0.0.1:8000/api/users/
- Métodos: GET, POST
- Descripción: retorna la lista de usuarios al hacer GET; mientras que si se hace POST, se crea un nuevo usuario.
### http://127.0.0.1:8000/api/users/1/
- Métodos: UPDATE, DELETE
- Descripción, obtiene un usuario específico (1) a este se le puede modificar o borrar. 
