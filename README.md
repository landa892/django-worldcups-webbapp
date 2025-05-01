
# World Cups Project


## Descripción

Este es un sitio web desarrollado con Django que presenta información sobre todos los Campeonatos Mundiales de Fútbol desde 1930 hasta la actualidad. El objetivo es mostrar detalles de cada edición, incluyendo país anfitrión, año, campeón, figuras destacadas y el once titular que jugó la final.

También se implementa autenticación de usuarios, perfiles y mensajería interna, además de un panel de administración para gestionar todo el contenido.

---

## Funcionalidades principales

- 📅 Listado completo de los mundiales.
- 🏆 Detalles de cada torneo: sede, campeón, once titular y descripción del camino al título.
- 🔐 Registro e inicio de sesión de usuarios.
- 🧑 Perfil de usuario con datos personales.
- 💬 Sistema de mensajes entre usuarios.
- 🛠️ Panel de administrador personalizado.

---

## Instalación y uso

1. Cloná el repositorio:

```bash
git clone https://github.com/tuusuario/proyecto-mundiales.git
cd proyecto-mundiales



1. Create virtual environment:
   ```
   python -m venv env
   source env/bin/activate
   ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Migrate:
   ```
   python manage.py migrate
   ```
4. Create superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run server:
   ```
   python manage.py runserver
   ```


- blog: World Cup info
- accounts: User profiles
- messages_app: User messaging

Acceso al panel de administración

URL: http://127.0.0.1:8000/admin/
Usuario: admin
Contraseña: admin08